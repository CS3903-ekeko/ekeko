from os import getenv

from flask import Flask

app = Flask(__name__)


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
