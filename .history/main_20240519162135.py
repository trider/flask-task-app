from flask import Flask, url_for
from markupsafe import escape

from api import api



app = Flask(__name__)
app.register_blueprint(api.bp)
print(app)

@app.route('/')
def index():
    return 'index'


# print('\n****************************************')
# print('flask-task-app: Ver', '0.1.1')
# print('****************************************\n')


if '__name__' == '__main__':
    print('****************************************')
    print('flask-task-app: Ver', '0.1.1')
    print('****************************************\n')
    app.run(host='0.0.0.0', port=5000, debug=True)





