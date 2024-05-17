from flask import Flask, Blueprint, request, redirect, url_for, session, g, flash, render_template,json
bp = Blueprint('api', __name__, url_prefix='/api')
from api import _utils as utils

   
@bp.route('/login')
def login():
    return 'login'
   

@bp.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'
   
 
@bp.route('/<command>/<target>', methods=['GET', 'POST']) 
def getUsers(command, target):
    if command == 'get':
        return utils.getCollection(target, {})
    else:
        return 'Invalid command'
       
       
@bp.route('/<target>/<command>/<val>', methods=['GET', 'POST']) 
def runCommand(command, target, val):
    if command == 'get':
        return utils.getCollection(target, {})
    else:
        return 'Invalid command'

