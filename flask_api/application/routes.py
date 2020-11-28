from application import db
import json

from flask import request, make_response
from flask import current_app as app
from .repositories import github_user as git_repository
from .facades.github_process import GitHubProcess

API_ENDPOINT = 'api/v1/'

@app.route('/')
def index():
    """Hello World."""
    return make_response("Hello World")


@app.route('/{}/users'.format(API_ENDPOINT))
def insert():
    """Return users from db"""
    page = request.args.get('page')
    per_page = request.args.get('per_page')

    page = int(page) if page else 1
    per_page = int(per_page) if per_page else 25

    db_users = git_repository.get_page(page, per_page)
    json_list=[i.serialize for i in db_users]
    return ({'users': json_list})

@app.route('/{}/create_db'.format(API_ENDPOINT))
def create_db():
    "Create dbs"
    db.drop_all()
    db.create_all()
    return ({"process": "success"})


@app.route('/{}/seed_db'.format(API_ENDPOINT))
def seed_db():
    "Download users from github api"
    total = request.args.get('total')
    total = int(total) if total else 150

    git_process = GitHubProcess()
    git_process.download_and_store(total)
    return ({"process": "success"})

@app.route('/{}/clean_db'.format(API_ENDPOINT))
def clean_db():
    "clean dbs"
    git_repository.clean_table()
    return ({"process": "success"})

