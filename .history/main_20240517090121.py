import Flask as flask

app = flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"