#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/cities_by_states')
def states_list():
    """Render template with states
    """
    path = '8-cities_by_states.html'
    states = storage.all(State)
    return render_template(path, states=states)


@app.teardown_appcontext
def app_teardown(arg=None):
    """Clean-up session
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
