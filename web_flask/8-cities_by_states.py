#!/usr/bin/python3
'''Flask module documentation for State City
listens to host='0.0.0.0', port=5000
renders the html page
'''
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def display_html():
    '''Displays the html page'''
    states = storage.all('State').values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close(exc):
    '''teardown closing storage'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
