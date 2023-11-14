#!/usr/bin/python3
'''Flask module documentation
Listens to host='0.0.0.0', port=5000
renders the html page'''
from flask import Flask, render_template
from models import storage
from models.city import City
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def display_html_filters():
    '''render html content'''
    states = storage.all(State).values()
    cities = storage.all(City).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states,
                           cities=cities, amenities=amenities)


@app.teardown_appcontext
def close(exc):
    '''teardown closing storage'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
