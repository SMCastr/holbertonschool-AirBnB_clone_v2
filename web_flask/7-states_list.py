#!/usr/bin/python3
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
    - /states_list: display an HTML page: (inside the tag BODY)
        H1 tag: "States"
        UL tag: with the list of all State objects present in DBStorage
        sorted by name (A->Z) tip
        LI tag: description of one State: <state.id>: <B><state.name></B>
Note: You must use the option strict_slashes=False in your route definition
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from flask import abort

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Route handler for /states_list
    Renders an HTML page displaying the list of states.
    """

    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)

    return render_template("7-states_list.html", states=sorted_states)


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
