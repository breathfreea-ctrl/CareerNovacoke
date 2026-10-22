import math

from flask import Flask, abort, render_template, request
from matching import match_user
from models import ROLES

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', roles=ROLES)

@app.route('/survey')
def survey():
  all_skills = sorted({
    skill
    for role in ROLES
    for skill in role["required_skills"]
  })
  
  
  all_interests = sorted({
    interest
    for role in ROLES
    for interest in role["interests"]
  })
  
  return render_template(
    'survey.html',
    skills=all_skills,
    interests=all_interests,
  )

@app.route('/results', methods=['POST'])
def results():

  user_skills = request.form.getlist("skills") 
  user_interests = request.form.getlist("interests")
  try:
    experience_years = float(
      request.form.get("experience_years", "0")
    )
    if not math.isfinite(experience_years):
      experience_years = 0
    experience_years = max(experience_years, 0)
  except ValueError:
    experience_years = 0

  matched_roles = match_user(
    user_skills,
    experience_years,
    user_interests,
  )

  return render_template(
    'results.html',
    roles=matched_roles,
    user_skills=user_skills,
    experience_years=experience_years,
    user_interests=user_interests,
  )


@app.route('/role/<int:role_id>')
def role_detail(role_id):
  role = next((role for role in ROLES if role["id"] == role_id), None)
  if role is None:
    abort(404)
  return render_template('role_detail.html', role=role)


if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5000, debug=False)