#!/usr/bin/python3
<<<<<<< HEAD
""" script that starts a Flask web application:
    Your web application must be listening on 0.0.0.0, port 5000
    Routes: /: display “Hello HBNB!”
            /hbnb: display “HBNB”
    You must use the option strict_slashes=False in your route definition """
=======
"""
starts a Flask web application
"""

>>>>>>> Mangoyi_Junior
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
def hello_hbnb():
    """ hello_hbnb method """
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def only_hbnb():
    """ only_hbnb method """
    return ('HBNB')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> Mangoyi_Junior
