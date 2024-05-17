from api import _utils as utils
from flask import Flask, Blueprint, request, redirect, url_for, session, g, flash, render_template, json
bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/login')
def login():
    return 'login'


@bp.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


@bp.route('/<command>/<collection>', methods=['GET', 'POST'])
def getUsers(command, collection):
    print(command, collection)
    if command == 'get':
        return utils.getCollection(collection, {})
    else:
        return 'Invalid command'
