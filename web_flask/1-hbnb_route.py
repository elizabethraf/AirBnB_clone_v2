#!/usr/bin/python3
"""
Display flask web application

"""

from flask import Flask

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False
app.url_map.strict_slashes = False

@app.route("/", methods=["GET"])
def hello():
    return "Hello HBNB!"

@app.route("/hbnb", methods=["GET"])
def hbnb():
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
