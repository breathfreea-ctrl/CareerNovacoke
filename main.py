from flask import Flask, render_template, request

import os
from matching import match_user
from models import ROLES

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')#路由绑定，渲染并展示首页，首页跳转进入问卷

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
    experience=all_experience,
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


if __name__ == '__main__':
  app.run(host="0.0.0.0", port=3000, debug=True)#change the port with the direction of deepseek.