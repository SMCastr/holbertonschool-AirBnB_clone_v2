#!/usr/bin/python3
"""
Script that starts a Flask web application.

The web application must be listening on:
    - Address: 0.0.0.0
    - Port: 5000
Use storage for fetching data from the storage engine (FileStorage or DBStorage)
=> from models import storage and storage.all(...)
To load all cities of a State:
    If your storage engine is DBStorage, you must use cities relationship
    Otherwise, use the public getter method cities
After each request, you must remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close()
Routes:
    /states: display an HTML page: (inside the tag BODY)
        H1 tag: “States”
        UL tag: with the list of all State objects present in DBStorage
        sorted by name (A->Z) tip
            LI tag: description of one State: <state.id>: <B><state.name></B>
    /states/<id>: display an HTML page: (inside the tag BODY)
        If a State object is found with this id:
            H1 tag: “State: ”
            H3 tag: “Cities:”
            UL tag: with the list of City objects linked to the State
                sorted by name (A->Z)
                LI tag: description of one City: <city.id>: <B><city.name></B>
        Otherwise:
            H1 tag: “Not found!”
Note: You must use the option strict_slashes=False in your route definition
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML page with a list of all States.

    States are sorted by name.
    """
    states = storage.all(State).values()
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    state = storage.get(State, id)
    cities = []
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
    return render_template("9-states.html", state=state, cities=cities)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
