#!/usr/bin/python3
'''Flask module documentation'''
from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    '''method to print'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    '''method to print'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_is(text):
    '''method to print'''
    text = text.replace('_', ' ')
    return f'C {escape(text)}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
