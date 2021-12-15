from os import getenv

from flask import Flask

app = Flask(__name__)


def main() -> None:
    app.run(port=int(getenv("PORT", 5000)), host=("0.0.0.0"))
