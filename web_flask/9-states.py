#!/usr/bin/python3
'''Flask module documentation for State City
listens to host='0.0.0.0', port=5000
renders the html page
'''
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def display_html():
    '''Displays the html page'''
    states = storage.all('State').values()
    return render_template('9-states.html', states=states, condition='states')


@app.route('/states/<id>', strict_slashes=False)
def display_html_id(id):
    '''Display the html with id'''
    states = storage.all('State').values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html',
                                   state=state, condition='state')
    return render_template('9-states.html', condition='not_found')


@app.teardown_appcontext
def close(exc):
    '''teardown closing storage'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
