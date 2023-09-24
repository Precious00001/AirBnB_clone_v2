#!/usr/bin/python3
"""
Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
storage.all()


@app.teardown_appcontext
def teardown_data(self):
    """
        Remove the current SQLAlchemy session.
    """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_id(id=None):
    """
        Displays an HTML page with info about <id>, if it exists.
    """
    info = []
    states = storage.all(State)
    if id is None:
        for q in states:
            info.append(states[q])
    else:
        id = 'State.' + id
        info = states.get(id)
    return render_template('9-states.html', states=info, id=id)
    return render_template('9-states.html', state=id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
