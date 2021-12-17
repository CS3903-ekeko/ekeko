from os import getenv
from json import loads, dumps

from flask import Flask, render_template, request, Response, session

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

@app.route('/authenticate', methods=['POST'])
def authenticate():
    body = loads(request.data)
    username: str = body['username']
    password: str = body['password']

    db_session = db.getSession(engine)
    users = db_session.query(entities.Trader).\
        filter(entities.Trader.username == username)

    db_session.close()
    for i in users:
        if (i.password == password):
            session['id'] = i.id

            response = {'msg': 'ok', 'id': i.id, 'username': username}
            return Response(dumps(response), mimetype='application/json')

    return Response('{"msg": "No"}', status=401, mimetype='application/json')

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

@app.route("/order", methods=["POST"])
def put_order():
    c = loads(request.data)

    order = entities.BuySellOrder(
        buy_or_sell = c["buy_or_sell"],
        stock       = c["stock"],
        currency    = c["currency"],
        price       = c["price"],
        amount      = c["amount"],
    )

    db_session = db.getSession(engine)
    db_session.add(order)
    db_session.commit()
    db_session.close()

    return Response(dumps({"msg": "ok"}), status=201)

@app.route("/market", methods=["POST"])
def create_market():
    c = loads(request.data)

    market = entities.Market(
        stock    = c["stock"],
        currency = c["currency"]
    )

    db_session = db.getSession(engine)
    db_session.add(market)
    db_session.commit()
    db_session.close()

    return Response(dumps({"msg": "ok"}), status=201)

@app.route("/market/<stock>/<currency>", methods=["GET"])
def market(stock: str, currency: str):
    # TODO: Return market template
    pass

def main() -> None:
    app.run(port=int(getenv("PORT", 5000)), host=("0.0.0.0"))
