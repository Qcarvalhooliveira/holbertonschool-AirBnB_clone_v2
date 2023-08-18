#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """List all cities by states"""
    state = storage.all(State)
    return render_template('8-cities_by_states.html', data=state)


@app.teardown_appcontext
def remove_session(execption):
    """Remove the current SQLAlchemy Session"""
    return storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
