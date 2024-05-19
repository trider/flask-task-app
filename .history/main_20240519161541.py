import Flask
from markupsafe import escape

from api import api



app = Flask(__name__)
app.register_blueprint(api.bp)




print('\n****************************************')
print('flask-task-app: Ver', '0.1.1')
print('****************************************\n')


if app == 'main':
    print('****************************************')
    print('flask-task-app: Ver', '0.1.1')
    print('****************************************\n')
    app.run(host='0.0.0.0', port=5000, debug=True)





