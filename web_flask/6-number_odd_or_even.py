#!/usr/bin/python3
"""
start flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """display “Hello HBNB!”"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB!"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """display “C ” followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return 'C ' + text


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text):
    """display “C ” followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return 'Python ' + text


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays a HTML page only if n is an integer and return odd or even"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        selection = 'even'
    else:
        selection = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           selection=selection)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
