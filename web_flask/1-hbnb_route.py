#!/usr/bin/python3
"""
flask model for route
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    """
        home route
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def index():
    """
        Displays 'HBNB'
    """
    return 'HBNB'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
