from flask import Flask, url_for
from markupsafe import escape

from api import api



app = Flask(__name__)
app.register_blueprint(api.bp)
print(__name__)

if app.name == '__main__':
    print('****************************************')
    print('flask-task-app: Ver', '0.1.1')
    print('****************************************\n')
    app.run(host='0.0.0.0', port=5000, debug=True)



