import hmac
import os
import secrets

from flask import Flask, abort, redirect, render_template, request, session, url_for

from survey_questions import QUESTIONS, validate_selection

app = Flask(__name__)
app.config.update(
    SECRET_KEY=os.environ["SESSION_SECRET"],
    SESSION_COOKIE_HTTPONLY=True,
    # The app also runs inside Replit's cross-site preview iframe.
    SESSION_COOKIE_SAMESITE="None",
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_PARTITIONED=True,
    MAX_CONTENT_LENGTH=16 * 1024,
)


def csrf_token():
    if "survey_csrf" not in session:
        session["survey_csrf"] = secrets.token_urlsafe(32)
    return session["survey_csrf"]


def check_csrf():
    provided = request.form.get("csrf_token", "")
    expected = session.get("survey_csrf", "")
    if not expected or not hmac.compare_digest(expected.encode(), provided.encode()):
        abort(400, description="页面已过期或请求无效，请刷新问卷后重试。")


def survey_state():
    if "survey_state" not in session:
        session["survey_state"] = {"step": 0, "answers": {}, "completed": False}
    return session["survey_state"]


@app.after_request
def protect_survey_responses(response):
    if request.path == "/results" or request.path.startswith("/survey"):
        response.headers["Cache-Control"] = "no-store"
    return response


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == "POST":
        check_csrf()
    if not QUESTIONS:
        return render_template(
            "survey.html", questions=[], current_index=0, total_questions=0,
            progress=0, answers={}, error=None, csrf_token=csrf_token(),
        )
    state = survey_state()
    question = QUESTIONS[state["step"]]
    error = None

    if request.method == "POST":
        if state["completed"]:
            return redirect(url_for("results"), code=303)
        if request.form.get("question_id") != question["id"]:
            # A browser Back/reload must not apply an old answer to a new step.
            return redirect(url_for("survey"), code=303)

        action = request.form.get("action")
        if action not in {"back", "next"}:
            abort(400, description="无效的问卷操作。")
        selected, error = validate_selection(
            question, request.form.getlist(question["id"]), required=action == "next"
        )
        if error is None:
            state["answers"][question["id"]] = selected
            if action == "back":
                state["step"] = max(0, state["step"] - 1)
            elif state["step"] < len(QUESTIONS) - 1:
                state["step"] += 1
            else:
                # Recheck every answer before accepting a completed questionnaire.
                for index, previous in enumerate(QUESTIONS):
                    _, previous_error = validate_selection(
                        previous, state["answers"].get(previous["id"], [])
                    )
                    if previous_error:
                        state["step"] = index
                        break
                else:
                    state["completed"] = True
            session["survey_state"] = state
            destination = "results" if state["completed"] else "survey"
            return redirect(url_for(destination), code=303)
        # Keep safe posted choices when displaying a validation error.
        answers = dict(state["answers"])
        allowed = {option["value"] for option in question["options"]}
        answers[question["id"]] = [
            value for value in request.form.getlist(question["id"]) if value in allowed
        ]
    else:
        if state["completed"]:
            return redirect(url_for("results"))
        answers = state["answers"]

    return render_template(
        "survey.html",
        questions=[question],
        current_index=state["step"] + 1,
        total_questions=len(QUESTIONS),
        progress=round((state["step"] + 1) * 100 / len(QUESTIONS)),
        answers=answers,
        error=error,
        csrf_token=csrf_token(),
    ), 422 if error else 200


@app.route('/survey/welcome')
def survey_welcome():
    return render_template('survey_welcome.html')


@app.route('/results')
def results():
    state = session.get("survey_state")
    if not state or not state["completed"]:
        return redirect(url_for("survey"))
    summary = [
        {
            "title": question["title"],
            "labels": [
                option["label"]
                for option in question["options"]
                if option["value"] in state["answers"].get(question["id"], [])
            ],
        }
        for question in QUESTIONS
    ]
    return render_template("results.html", summary=summary, csrf_token=csrf_token())


@app.post('/survey/edit')
def edit_survey():
    check_csrf()
    state = survey_state()
    state["step"] = 0
    state["completed"] = False
    session["survey_state"] = state
    return redirect(url_for("survey"), code=303)


@app.post('/survey/restart')
def restart_survey():
    check_csrf()
    session.pop("survey_state", None)
    session.pop("survey_csrf", None)
    return redirect(url_for("survey"), code=303)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)