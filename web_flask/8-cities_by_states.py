#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models.city import City
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """List all cities by states"""
    states = storage.all(State).values()
    result = []
    for state in sorted(states, key=lambda x: x.name):
        result.append([state, state.cities])
    return render_template('8-cities_by_states.html', result=result)


@app.teardown_appcontext
def remove_session(execption):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
