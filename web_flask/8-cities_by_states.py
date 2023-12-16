#!/usr/bin/python3
"""
Script that starts a Flask web application.

The web application must be listening on:
    - Address: 0.0.0.0
    - Port: 5000
Use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
After each request you must remove the current SQLAlchemy Session:
    - Declare a method to handle @app.teardown_appcontext
    - Call in this method storage.close()
Routes:
    - /cities_by_states: display an HTML page: (inside the tag BODY)
        H1 tag: "States"
        UL tag: with the list of all State objects present in DBStorage
        sorted by name (A->Z) tip
        LI tag: description of one State: <state.id>: <B><state.name></B>
        + UL tag: with the list of City objects linked to the State
        sorted by name (A->Z)
        LI tag: description of one City: <city.id>: <B><city.name></B>
Note: You must use the option strict_slashes=False in your route definition
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays an HTML page with a list of all states and related cities."""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
