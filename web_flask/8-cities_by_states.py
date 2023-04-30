#!/usr/bin/python3
<<<<<<< HEAD
""" this module contains a script that starts a Flask web application
    the web application must be listening on 0.0.0.0, port 5000
    Routes: - /states_list """
from models import *
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from flask import Flask, render_template
app = Flask(__name__)
classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}
=======
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)
>>>>>>> Mangoyi_Junior


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
<<<<<<< HEAD
    """ display HTML page with list of cities """
    states = storage.all(classes["State"]).values()
    # ^ fetches states data from storage engine, then in line below,
    # those states are passed into the template
=======
    """display the states and cities listed in alphabetical order"""
    states = storage.all("State").values()
>>>>>>> Mangoyi_Junior
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
<<<<<<< HEAD
def remove_SQLalc_session(exception):
    """ close storage when tear down is called """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> Mangoyi_Junior
