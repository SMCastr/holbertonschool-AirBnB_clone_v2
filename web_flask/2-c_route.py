#!/usr/bin/python3

The web application must be
listening on: 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable

NOTE: You must use the option strict_slashes=False in your route definition
"""

from flask import Flask


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


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
