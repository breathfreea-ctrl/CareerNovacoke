# Running the imported homepage

- Stack: Python / Flask, keeping the existing project structure.
- Run the **Start application** workflow, or run `python main.py`.
- The server listens on `0.0.0.0:5000` and renders the existing
  `templates/index.html` at `/`.
- Dependencies are recorded in `pyproject.toml` and `uv.lock`.
- No external services are needed. `SESSION_SECRET` is required to sign the
  questionnaire's session cookie; configure it through Replit Secrets.

## Current scope

The homepage's exploration links navigate to `/survey/welcome`, a questionnaire
welcome page based on the user's supplied Jinja template. It shares the
homepage's typography, diagonal pale-yellow/pink gradient, and sage buttons.
The reusable layout is in `templates/base.html`, with styles in
`static/survey.css`.

The welcome page's Start form opens `/survey`. Three basic steps cover skills,
experience, and interests, configured in `survey_questions.py`. GET displays the
current step; POST validates an answer and moves Back/Next/Submit. Each valid
POST redirects to avoid re-submitting on refresh. Multi-select questions require
at least one choice; going Back does not require completing the current step.

Answers and the current step are held in a signed browser-session cookie, not
a database; the cookie is signed, not encrypted. Do not collect sensitive
personal data in these questions. Cookies use Secure, HttpOnly, SameSite=None,
and Partitioned so the session works inside the cross-site preview iframe.
POSTs are CSRF-protected, and survey/summary responses use `Cache-Control:
no-store`. Browser sessions are independent.

`/results` shows a readable answer summary only after completion. Users can edit
their saved answers or clear them and restart, using POST forms.

The imported `matching.py` is empty, and `models.py`
contains incomplete data and a merge-conflict remnant. These remain untouched;
do not import them into public-page routes until matching is built. The summary
does not produce career recommendations, matching scores, or salary claims.

## Checks

Run `python -m unittest discover -s tests` for questionnaire flow checks.
