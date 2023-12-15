#!/usr/bin/python3
"""
Script that starts a Flask web application.

The web application must be
listening on:
    Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB'
    /c/<text>: Displays 'C' followed by the value of <text>
    /python/<text>: Displays 'Python' followed by the value of <text>
    /number/<n>: Displays 'n is a number' only if <n> is an integer
    /number_template/<n>: Displays a HTML page only if <n> is an integer:
        H1 tag: 'Number: n' inside the tag BODY
    /number_odd_or_even/<n>: Displays a HTML page only if <n> is an integer:
        H1 tag: 'Number: n is even|odd' inside the tag BODY
NOTE: You must use the option strict_slashes=False in your route definition
"""

from flask import Flask, render_template
from flask import abort


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL ("/")
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Route handler for "/hbnb"
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Route handler for "/c/<text>"
    """

    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python(text="is_cool"):
    """
    Route handler for "/python/<text>"
    """

    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Route handler for "/number/<n>"
    """
    if not isinstance(n, int):
        abort(404)
    return "{} is a number".format(n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    Route handler for "/number_odd_or_even/<n>"
    """

    result = "even" if n % 2 == 0 else "odd"

    return render_template("6-number_odd_or_even.html", number=n, parity=result)


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
