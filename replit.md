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
homepage's diagonal pale-yellow/pink gradient and sage buttons.
The reusable layout is in `templates/base.html`, with styles in
`static/survey.css`.

Only the homepage uses the handwritten brush/KaiTi style. All other pages use
clean sans-serif typography: DM Sans for Latin text and Noto Sans SC for Chinese,
with platform sans-serif fallbacks.

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

`/results` shows a career exploration report and answer summary after completion.
Users can download their answers at `/survey/answers.json`, edit their saved
answers or clear them and restart using CSRF-protected POST forms. `/roles/<id>`
shows a personalized reference detail page after completion.

The repaired imported catalog in `models.py` contains seven careers, not ten.
`matching.py` maps the broad survey categories to each career: skill coverage
contributes up to 60 points and interest coverage up to 40, rounded separately
and summed. Results at or above 20 points are sorted by score then source ID;
at most three are shown. Years of general experience affect learning suggestions
only, not ranking. The rules and limitations are disclosed in the report.

This is exploratory self-report matching, not validated aptitude testing,
qualification assessment or employment probability. Missing checked categories
are not proven skill deficits. Never fabricate mentors, employment timeframes or
target countries: these are not collected. Imported salary and market-growth
claims have not been verified and must not be displayed as authoritative facts.

## Checks

Run `python -m unittest discover -s tests` for questionnaire flow checks.
