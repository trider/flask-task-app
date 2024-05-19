from api import _utils as utils
from flask import Flask, Blueprint, request
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
    print(target, command, category, val)
    data = None
    request = request
    if request.method == 'GET':
        data = request
    elif request.method == 'POST':
       data = request.json
    
    if target == 'users':
    
        
        return utils.usersManage(command, category, val)
    elif target == 'tasks':
     if request.method == 'GET':
        return utils.tasksManage(command, category, val, data)
     elif request.method == 'POST':
        return utils.tasksManage(command, category, val, data)
    else:
        return 'Invalid command'
