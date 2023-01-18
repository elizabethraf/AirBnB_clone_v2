#!/usr/bin/python3
"""
Display flask web application

"""

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    """Display "Hello HBNB!" """
    return "Hello HBNB!"

@app.route("/hbnb", methods=["GET"])
def hbnb():
     """Display “HBNB” """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
