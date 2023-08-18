#!/usr/bin/python3
"""script that starts a Flask web application"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def state_list():
    """Display a HTML page of state"""
    state = storage.all(State)
    return render_template("9-states.html", states=state, mode="state")


@app.route("/states/<id>")
def states_id(id):
    """show id for the states"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state,
                                   mode="state_id")
    return render_template("9-states.html", states=state, mode="none")


@app.teardown_appcontext
def teardown(execption):
    """closing storage"""
    return storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
