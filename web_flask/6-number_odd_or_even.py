#!/usr/bin/python3
"""flask"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """hello HBNB route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """HBNB route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    """C route"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n=None):
    if n % 2 == 0:
        strang = "even"
    else:
        strang = "odd"
    return render_template('6-number_odd_or_even.html', n=n, strang=strang)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
