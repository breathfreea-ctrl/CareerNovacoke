from flask import Flask, redirect, render_template, request, session, url_for

from matching import generateLearningPlan, match_user
from models import ROLES, SCHEMA

app = Flask(__name__)
app.secret_key = "career-survey-local-session-key"


def _question_is_visible(question, answers):
    """判断条件题是否应显示。"""
    condition = question.get("when")

    if not condition:
        return True

    if condition == "a.path === 'A' || a.ready === 'YES'":
        return answers.get("path") == "A" or answers.get("ready") == "YES"

    if condition == "a.path === 'B'":
        return answers.get("path") == "B"

    if condition == "a.path === 'B' && a.ready === 'NO'":
        return answers.get("path") == "B" and answers.get("ready") == "NO"

    return True


def _survey_steps(answers):
    """获取当前答案下需要显示的题目，并整理选项格式。"""
    questions = []

    for question in SCHEMA:
        if question.get("id") == "welcome":
            continue
        if not _question_is_visible(question, answers):
            continue
        questions.append(question)

    if answers.get("path") == "B":
        order = {
            "path": 0,
            "ready": 1,
            "skills": 2,
            "interest": 3,
            "time": 4,
            "salary": 5,
            "country": 6,
            "reality": 7,
        }
        questions.sort(
            key=lambda question: order.get(question.get("id"), 99)
        )

    prepared = []

    for question in questions:
        item = dict(question)
        item["options"] = []

        if question.get("type") == "groupedMulti":
            for group in question.get("groups", []):
                for child in group.get("children", []):
                    item["options"].append({
                        "value": child["label"],
                        "label": child["label"],
                    })
            item["input_type"] = "checkbox"
        else:
            for option in question.get("options", []):
                item["options"].append({
                    "value": option["v"],
                    "label": option["t"],
                })
            item["input_type"] = "radio"

        if question.get("type") == "notice":
            item["title"] = question.get("text", "")
            item["options"] = []
            item["required"] = False

        prepared.append(item)

    return prepared


def _clear_dependent_answers(answers):
    """切换职业路径时清除依赖旧路径的答案。"""
    for key in (
        "skills",
        "skills_majors",
        "skills_detail",
        "interest",
        "interest_majors",
        "interest_detail",
        "time",
        "salary",
        "country",
        "ready",
    ):
        answers.pop(key, None)


def _next_unanswered_index(questions, answers):
    """定位下一道当前分支中尚未回答的题目。"""
    for index, question in enumerate(questions):
        if question.get("type") == "notice":
            return index
        if question["id"] not in answers:
            return index
    return None


@app.route("/")
def index():
    session.pop("survey_answers", None)
    session.pop("survey_index", None)
    return render_template("index.html")


@app.route("/survey", methods=["GET", "POST"])
def survey():
    answers = dict(session.get("survey_answers", {}))
    questions = _survey_steps(answers)

    if not questions:
        return redirect(url_for("index"))

    try:
        current_index = int(session.get("survey_index", 0))
    except (TypeError, ValueError):
        current_index = 0
    current_index = max(0, min(current_index, len(questions) - 1))

    if request.method == "POST":
        action = request.form.get("action", "next")
        current_question = questions[current_index]
        question_id = current_question["id"]

        if action == "back":
            session["survey_index"] = max(0, current_index - 1)
            return redirect(url_for("survey"))

        if current_question.get("type") == "notice":
            session.pop("survey_answers", None)
            session.pop("survey_index", None)
            return redirect(url_for("index"))

        if current_question.get("type") == "groupedMulti":
            allowed_values = {
                option["value"] for option in current_question.get("options", [])
            }
            value = [
                item for item in request.form.getlist(question_id)
                if item in allowed_values
            ]
            if current_question.get("required") and not value:
                return render_template(
                    "survey.html",
                    questions=[current_question],
                    current_index=current_index + 1,
                    total_questions=len(questions),
                    progress=round(
                        current_index / max(len(questions), 1) * 100
                    ),
                    error="Please select at least one option.",
                )
        else:
            value = request.form.get(question_id, "")
            allowed_values = {
                option["value"] for option in current_question.get("options", [])
            }
            if value not in allowed_values:
                value = ""
            if current_question.get("required") and not value:
                return render_template(
                    "survey.html",
                    questions=[current_question],
                    current_index=current_index + 1,
                    total_questions=len(questions),
                    progress=round(
                        current_index / max(len(questions), 1) * 100
                    ),
                    error="Please complete this question first.",
                )

        if question_id == "path":
            _clear_dependent_answers(answers)

        answers[question_id] = value
        session["survey_answers"] = answers

        # 根据已回答的题目 ID 找下一题，避免条件分支变化时跳题。
        questions = _survey_steps(answers)
        next_index = _next_unanswered_index(questions, answers)

        if next_index is None:
            session.pop("survey_index", None)
            return redirect(url_for("results"))

        session["survey_index"] = next_index
        return redirect(url_for("survey"))

    current_question = questions[current_index]
    progress = round(current_index / max(len(questions), 1) * 100)

    return render_template(
        "survey.html",
        questions=[current_question],
        current_index=current_index + 1,
        total_questions=len(questions),
        progress=progress,
        error=None,
    )


@app.route("/results")
def results():
    answers = session.get("survey_answers", {})
    if not answers:
        return redirect(url_for("index"))

    all_results = match_user(answers)
    top_results = [
        role for role in all_results if role["totalPoints"] >= 34
    ][:3]

    for role in top_results:
        role["learning_plan"] = generateLearningPlan(role, answers)

    return render_template("results.html", results=top_results)


@app.route("/role/<int:role_id>")
def role_detail(role_id):
    role = next(
        (item for item in ROLES if item.get("id") == role_id),
        None,
    )
    if role is None:
        return redirect(url_for("results"))

    return render_template("role_detail.html", role=role)


if __name__ == "__main__":
    app.run(debug=True)