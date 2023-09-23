#!/usr/bin/python3
"""flask model
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """Return string when route queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return string when route queried
    """
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Outputs 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
