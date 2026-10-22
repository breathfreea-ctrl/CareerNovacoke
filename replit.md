# Career explorer

## Run on Replit
- This imported project remains a Python 3.12 Flask application with Jinja templates.
- Click Run to start the `Start application` workflow, using
  `python -m gunicorn --bind 0.0.0.0:5000 main:app`.
- Dependencies are recorded in `pyproject.toml` and `uv.lock`.
- For direct development, `python main.py` also serves on port 5000.
- No database, credentials, or external services are required.

## Pages and behavior
- `/`: career catalog and survey entry.
- `/survey`: skills, interests, and experience form.
- `/results`: POST-only results ranked by skill and interest overlap.
- `/role/<id>`: the supplied career details.
- Run checks with `python -m unittest discover -s tests -v`.

## Matching and data limitations
- The imported matching module and templates were empty. The initial working
  implementation scores 70% required-skill coverage and 30% interest coverage.
- Experience is displayed as context only: no experience criteria were provided
  in the imported career data. Scores are not professional suitability assessments.
- Career descriptions, salaries, trends, and source labels are preserved from
  the repository and have not been independently verified.
- Survey responses are processed for the request only and are not stored.
