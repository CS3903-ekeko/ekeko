from os import getenv

from flask import Flask, render_template

from .database import connector

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

@app.route('/', methods = ['GET'])
def get_index():
    return render_template('index.html')


@app.route("/user")
def user():
    pass

@app.route("/order")
def order():
    pass

@app.route("/market")
def market():
    pass

def main() -> None:
    app.run(port=int(getenv("PORT", 5000)), host=("0.0.0.0"))
