#!/usr/bin/python3
'''Starts a Flask Web app'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonText(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def numInt(n):
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
