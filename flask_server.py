from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/namecount/<name>")
def hello_count(name):
    safename = escape(name)
    Nchars = len(safename)
    return f"Hello, {safename}! Your name is {Nchars} characters long!"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route("/seq_complement/<seq>")
def seq_complement(seq):
    return f"{escape(seq)}"

