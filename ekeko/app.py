from os import getenv
from json import loads, dumps

from flask import Flask, render_template, request, Response

from .database import connector
from .model import entities

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

@app.route('/', methods = ['GET'])
def get_index():
    return render_template('index.html')


@app.route("/user", methods=["POST"])
def create_user():
    c = loads(request.data)

    user = entities.Trader(
        username = c["username"],
        password = c["password"]
    )

    db_session = db.getSession(engine)
    db_session.add(user)
    db_session.commit()
    db_session.close()

    return Response(dumps({"msg": "ok"}), status=201)

@app.route("/order")
def order():
    pass

@app.route("/market")
def market():
    pass

def main() -> None:
    app.run(port=int(getenv("PORT", 5000)), host=("0.0.0.0"))
