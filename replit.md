# Running the imported homepage

- Stack: Python / Flask, keeping the existing project structure.
- Run the **Start application** workflow, or run `python main.py`.
- The server listens on `0.0.0.0:5000` and renders the existing
  `templates/index.html` at `/`.
- Dependencies are recorded in `pyproject.toml` and `uv.lock`.
- No secrets or external services are needed to view the homepage.

## Current scope

The homepage's exploration links navigate to `/survey/welcome`, a questionnaire
welcome page based on the user's supplied Jinja template. It shares the
homepage's typography, diagonal pale-yellow/pink gradient, and sage buttons.
The reusable layout is in `templates/base.html`, with styles in
`static/survey.css`.

The welcome page's Start form submits a GET request to `/survey`. Questionnaire
questions and matching are not implemented yet, so this destination renders a
styled, explicit HTTP 501 notice with links back to the welcome page and home.
No survey answers are collected or stored.

The imported `matching.py` and results template are empty, and `models.py`
contains incomplete data and a merge-conflict remnant. These remain untouched;
do not import them into public-page routes until the matching feature is built.
