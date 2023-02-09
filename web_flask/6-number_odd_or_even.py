#!/usr/bin/python3
"""
Display scriopt that start a flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Display "Hello HBNB!" """

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def index():
    """Display "Hello HBNB!" """

    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def text():
    """Display “C”  with text"""

    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is_cool"):
    """Display “Python ”  <text> variable"""

    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Display “n is a number” if n is an integer"""

    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def show_text4(n):
    """Defines '/number_template/' route of a variable"""
    if isinstance(n, int):

        return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def show_text5(n):
    """
    method that defines '//number_odd_or_even/' route that uses a variable
    """
    if n % 2 == 0:
        num_string = "Number: {} is even".format(n)

    elif n % 2 != 0:
        num_string = "Number: {} is odd".format(n)

    return render_template('6-number_odd_or_even.html', num_string=num_string)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)