from api import _utils as utils
from flask import Flask, Blueprint, request, redirect, url_for, session, g, flash, render_template, json
bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/login')
def login():
    return 'login'


@bp.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


@bp.route('/<target>/<command>/<collection>', methods=['GET', 'POST'])
def getUsers(target, command, category):
    print(target, command, category)
    if target == 'users':
        return utils.manageUsers(command, category)
    else:
        return 'Invalid command'