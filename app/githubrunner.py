import os
import zipfile
from os import listdir
from urllib import request, parse


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_github_source():
    targetpath = "../tmp/game"
    ensure_dir(targetpath)
    zippath = "../tmp/game.zip"
    githubuser = 'paulokow'
    githubproject = 'consoledemo'
    projectbranch = 'master'
    mainfile = 'main.py'
    return get_github_source_with_params(githubproject, githubuser, mainfile, projectbranch, targetpath, zippath)


def get_github_source_with_params(githubproject, githubuser, mainfile, projectbranch, targetpath, zippath):
    request.urlretrieve('https://github.com/{}/{}/archive/{}.zip'.format(githubuser, githubproject, projectbranch),
                        zippath)
    with zipfile.ZipFile(zippath, "r") as zip_ref:
        zip_ref.extractall(targetpath)
    unpackedpath = '{}/{}-{}'.format(targetpath, githubproject, projectbranch)
    onlyfiles = [f for f in listdir(unpackedpath) if f.endswith('.py')]
    output = ''
    if mainfile in onlyfiles:
        with open('{}/{}'.format(unpackedpath, mainfile), 'r') as f:
            output += f.read()
    for file in onlyfiles:
        if file != mainfile:
            output += '\n----{' + file + '}----\n'
            with open('{}/{}'.format(unpackedpath, file), 'r') as f:
                output += f.read()
    output = parse.quote(output)
    return output
