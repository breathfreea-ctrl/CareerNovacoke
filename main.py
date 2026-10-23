from flask import Flask, abort, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/survey')
def survey():
    # Keep the Start destination explicit until the questionnaire is implemented.
    return render_template('survey.html'), 501


@app.route('/survey/welcome')
def survey_welcome():
    return render_template('survey_welcome.html')


@app.route('/results', methods=['POST'])
def questionnaire_unavailable():
    # Do not load the unfinished matching/data modules to display public pages.
    abort(501, description="问卷与职业匹配功能尚未实现。请返回首页浏览。")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)