#!/usr/bin/python3
'''Flask module documentation'''
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_html():
    '''Displays the html page'''
    states = storage.all('State')
    return render_template('7-states_list.html', list=states)


@app.teardown_appcontext
def close():
    '''teardown closing storage'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
