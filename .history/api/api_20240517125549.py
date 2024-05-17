from flask import Flask, Blueprint, request, redirect, url_for, session, g, flash, render_template,json
bp = Blueprint('api', __name__, url_prefix='/api')
import _utils as utils

   
@bp.route('/login')
def login():
    return 'login'
   

@bp.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'
   
 
@bp.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

