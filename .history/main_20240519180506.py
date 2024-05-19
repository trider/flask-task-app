
import flask
from flask import Flask, url_for
from api import api



app = Flask(__name__)
app.register_blueprint(api.bp)
print(app)

@app.route('/')
def index():
    return 'index'





if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    print('\n****************************************')
    print('flask-task-app: Ver', '0.1.1')
    print('****************************************\n')
    app.debug = True
    app.run()





fla