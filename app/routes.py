from app import app
from urllib import request
import zipfile

from os import listdir, getcwd
from os.path import isfile, join
import os

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/unzip')
def unzip():
    targetpath = "../tmp/game"
    ensure_dir(targetpath)
    zippath = "../tmp/game.zip"
    request.urlretrieve('https://github.com/paulokow/python_console_player/archive/master.zip', zippath)
    with zipfile.ZipFile(zippath, "r") as zip_ref:
        zip_ref.extractall(targetpath)
    onlyfiles = [f for f in listdir(targetpath + '/python_console_player-master')]
    return '{}'.format(onlyfiles)


@app.route('/cwd')
def cwd():
    cwd = getcwd()
    return 'Current path: {}'.format(cwd)