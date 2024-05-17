import datetime, json, re, requests
from api import _utils as utils
from flask import Flask, Blueprint, request, redirect, url_for, session, g, flash, render_template, json
bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/login')
def login():
    return 'login'


@bp.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


@bp.route('/<target>/<command>/<category>', methods=['GET', 'POST'])
@bp.route('/<target>/<command>/<category>/<val>', methods=['GET', 'POST'])
def getUsers(target, command, category, val=None):
    print(target, command, category, val, request)
    if target == 'users':
        return utils.usersManage(command, category, val, request.json)
    elif target == 'tasks':
        return utils.tasksManage(command, category, val, request.json)
    else:
        return 'Invalid command'
