#!/usr/bin/python3
"""
Display scriopt that start a flask web application

"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Display "Hello HBNB!" """

    return "Hello HBNB!"

@app.route('/airbnb-onepage', strict_slashes=False)
def index():
    """Display "Hello HBNB!" """

    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
