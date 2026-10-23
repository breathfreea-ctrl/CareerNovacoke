# Running the imported homepage

- Stack: Python / Flask, keeping the existing project structure.
- Run the **Start application** workflow, or run `python main.py`.
- The server listens on `0.0.0.0:5000` and renders the existing
  `templates/index.html` at `/`.
- Dependencies are recorded in `pyproject.toml` and `uv.lock`.
- No secrets or external services are needed to view the homepage.

## Current scope

This restoration serves the existing standalone homepage without changing its
design. The homepage already explains, through its existing button handlers,
that the questionnaire has not been implemented.

The imported survey/results templates and `matching.py` are empty, and
`models.py` contains incomplete data and a merge-conflict remnant. These were
left untouched rather than inventing matching behavior during a request to
reopen the homepage. Direct requests to the unfinished questionnaire routes
return an explicit HTTP 501 instead of an empty page or a startup crash.
