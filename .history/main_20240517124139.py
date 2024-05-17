from flask import Flask, url_for
from markupsafe import escape

from api import api



app = Flask(__name__)
app.register_blueprint(api.bp)

@app.route('/')
def index():
    return 'index'



# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))



