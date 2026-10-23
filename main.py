import os

from flask import Flask, abort, redirect, render_template, request, session, url_for

from matching import generate_learning_plan, get_tier, match_user
from models import ROLES, SCHEMA


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-secret-key-before-deployment")
app.config.update(
    SESSION_COOKIE_NAME="career_survey_session",
    SESSION_COOKIE_PATH="/",
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="None",
    SESSION_COOKIE_SECURE=True,
)

def get_answers():
    """Read the survey answers saved in the user's session."""
    answers = session.get("answers", {})
    return answers if isinstance(answers, dict) else {}


def get_active_steps(answers):
    """Return the questions shown for the selected career path."""
    path = answers.get("path")
    visible_ids = {"path"}

    if path in {"A", "B"}:
        visible_ids.update({
            "skills",
            "interest",
            "time",
            "salary",
            "country",
        })

    if path == "B":
        visible_ids.add("ready")

    return [
        question
        for question in SCHEMA
        if question.get("id") in visible_ids
    ]


def save_current_answer(question, answers):
    """Read the current question's answer from the submitted form."""
    question_id = question["id"]
    question_type = question.get("type")

    if question_type == "single":
        new_value = request.form.get(question_id, "").strip()

        # Changing the path invalidates answers from the previous path.
        if question_id == "path" and answers.get("path") != new_value:
            for key in (
                "skills",
                "skills_majors",
                "skills_detail",
                "interest",
                "interest_majors",
                "time",
                "salary",
                "country",
                "ready",
            ):
                answers.pop(key, None)

        if new_value:
            answers[question_id] = new_value

    elif question_type == "groupedMulti":
        selected = request.form.getlist(question_id)
        answers[question_id] = selected

        detail_key = f"{question_id}_detail"
        details = answers.get(detail_key, {})

        if question.get("hasFollowUp"):
            # The survey template should name these fields years__<skill>
            # and cert__<skill>, using the skill label in the field name.
            details = {}
            for label in selected:
                years = request.form.get(f"years__{label}", "").strip()
                cert = request.form.get(f"cert__{label}", "").strip()
                details[label] = {"years": years, "cert": cert}

            answers[detail_key] = details

    return answers


def validate_answer(question, answers):
    """Return an error message when a required answer is incomplete."""
    if not question.get("required", False):
        return None

    question_id = question["id"]

    if question.get("type") == "groupedMulti":
        selected = answers.get(question_id, [])
        if not selected:
            return "Please select at least one option."

        if question.get("hasFollowUp"):
            details = answers.get(f"{question_id}_detail", {})
            for label in selected:
                row = details.get(label, {})
                if not row.get("years") or not row.get("cert"):
                    return f'Please complete the experience and certification fields for "{label}".'

        return None

    if not answers.get(question_id):
        return "Please complete this question first."

    return None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/survey", methods=["GET", "POST"])
def survey():
    answers = get_answers()
    steps = get_active_steps(answers)

    if not steps:
        session.clear()
        return redirect(url_for("index"))

    if request.method == "GET" and request.args.get("reset") == "1":
        session.clear()
        answers = {}
        steps = get_active_steps(answers)

    if request.method == "POST":
        question_id = request.form.get("question_id", "")
        action = request.form.get("action", "next")

        question = next(
            (
                item for item in steps
                if isinstance(item, dict) and item.get("id") == question_id
            ),
            None,
        )
        if question is None:
            abort(400, description="The submitted question is not part of this survey path.")

        answers = save_current_answer(question, answers)
        print("POST 表单：", request.form.to_dict(flat=False))
        print("保存的答案：", answers)
        print("后续步骤：", [item["id"] for item in get_active_steps(answers)])
        steps = get_active_steps(answers)

        # The step list can change after answering the path question.
        question_ids = [item["id"] for item in steps]
        if question_id not in question_ids:
            question_id = steps[0]["id"]

        current_index = question_ids.index(question_id)
        error = None

        if action != "back":
            error = validate_answer(question, answers)

        if error:
            session["answers"] = answers
            print("POST 下一题：", question_id)
            session["current_id"] = question_id
            session.modified = True
            return render_template(
                "survey.html",
                question=question,
                answers=answers,
                error=error,
                step_number=current_index + 1,
                total_steps=get_total_steps(answers),
                is_last=is_final_question(question_id, answers),
            )

        if action == "back":
            if current_index > 0:
                question_id = steps[current_index - 1]["id"]
        elif current_index == len(steps) - 1:
            session["answers"] = answers
            session.pop("current_id", None)
            session.modified = True
            return redirect(url_for("results"))
        else:
            question_id = steps[current_index + 1]["id"]

        session["answers"] = answers
        session["current_id"] = question_id
        session.modified = True

        print("POST 下一题：", question_id)
        print("POST session：", dict(session))

        response = redirect(url_for("survey"))
        print("响应是否设置 session cookie：", "Set-Cookie" in response.headers)
        return response
    print("GET session：", dict(session))
    print(
        "GET 是否收到 session cookie：",
        bool(request.cookies.get(app.config.get("SESSION_COOKIE_NAME", "session")))
    )

    current_id = session.get("current_id", steps[0]["id"])
    current_index = next(
        (index for index, item in enumerate(steps) if item["id"] == current_id),
        0,
    )
    question = steps[current_index]

    return render_template(
        "survey.html",
        question=question,
        answers=answers,
        error=None,
        step_number=current_index + 1,
        total_steps=get_total_steps(answers),
        is_last=is_final_question(question["id"], answers),
    )


@app.route("/results")
def results():
    answers = get_answers()
    if not answers.get("path"):
        return redirect(url_for("index"))

    all_results = match_user(answers)
    top_results = [
        role for role in all_results if role.get("totalPoints", 0) >= 34
    ][:3]

    results_with_details = []
    for role in top_results:
        results_with_details.append(
            {
                **role,
                "tier": get_tier(role["totalPoints"]),
                "learning_plan": generate_learning_plan(role, answers),
            }
        )

    return render_template(
        "results.html",
        results=results_with_details,
        answers=answers,
    )


@app.route("/role/<role_id>")
def role_detail(role_id):
    role = next((item for item in ROLES if item["id"] == role_id), None)
    if role is None:
        abort(404)

    answers = get_answers()
    matched_role = next(
        (item for item in match_user(answers) if item["id"] == role_id),
        None,
    ) if answers else None

    return render_template(
        "role_detail.html",
        role=role,
        match=matched_role,
        tier=get_tier(matched_role["totalPoints"]) if matched_role else None,
        learning_plan=(
            generate_learning_plan(role, answers)
            if matched_role
            else None
        ),
    )

def get_total_steps(answers):
    # A 路径有 6 题；B 路径多一道准备度题，共 7 题。
    return 6 if answers.get("path") == "A" else 7


def is_final_question(question_id, answers):
    if answers.get("path") == "A":
        return question_id == "country"
    if answers.get("path") == "B":
        return question_id == "ready"
    return False

if __name__ == "__main__":
    app.run(debug=True)