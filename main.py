from flask import Flask, abort, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/survey')
@app.route('/results', methods=['POST'])
def questionnaire_unavailable():
    # The imported homepage is complete, but its questionnaire is not implemented.
    # Do not load the unfinished matching/data modules just to display the homepage.
    abort(501, description="问卷与职业匹配功能尚未实现。请返回首页浏览。")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)