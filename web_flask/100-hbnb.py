#!/usr/bin/python3
from flask import Flask
from models.state import State
from models.amenity import Amenity
from flask import render_template
from models import storage
from models.place import Place
"""
Start web application with two routings
"""
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
        storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Render template with states"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    print(places)
    return render_template('100-hbnb.html',
                           states=states,
                           places=places,
                           amenities=amenities)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
