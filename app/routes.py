from app import app
from flask import render_template
from app.githubrunner import get_github_source


@app.route('/')
@app.route('/index')
def index():
    output = get_github_source()
    return render_template('embed_trinket.html', code = output)

@app.route('/unzip')
def unzip():
    output = get_github_source()
    return render_template('link_trinket.html', code = output)

