#!/usr/bin/python3#!/usr/bin/python3
"""
Script that starts a Flask web application.

The web application must be listening on:
    - Address: 0.0.0.0
    - Port: 5000
Use storage for fetching data from the storage engine
(FileStorage or DBStorage)
=> from models import storage and storage.all(...)
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

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from flask import abort

app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    Route handler for /cities_by_states
    Renders an HTML page displaying the list of states and cities.
    """

    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)

    return render_template("8-cities_by_states.html", states=sorted_states)


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
