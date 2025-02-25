#!/usr/bin/python3
""" A script that starts a flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ displays 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ displays 'C' followed  by the value of the text variable
        (replace underscore _ symbols with a space )
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """ displays 'Python' followed  by the value of the text variable
        (replace underscore _ symbols with a space )
    """
    return 'Python ' + text.replace('_', ' ')


if __name__ == "__main__":
    """ run flask web app """
    app.run(host='0.0.0.0', port=5000)
