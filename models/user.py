#!/usr/bin/python3
<<<<<<< HEAD
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
=======
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
>>>>>>> Mangoyi_Junior
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
<<<<<<< HEAD
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column('email', String(128), nullable=False)
    password = Column('password', String(128), nullable=False)
    first_name = Column('first_name', String(128), nullable=True, default="NULL")
    last_name = Column('last_name', String(128), nullable=True, default="NULL")
    # backref may need to be back_populates?Below line commented out bc console
    # would not run with it in. This line was implemented in Task 8
    places = relationship("Place", cascade="delete", backref="user")
    # Below line is commented out for caution and was added in Task 9
    reviews = relationship("Review", cascade="delete", backref="user")
=======
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
>>>>>>> Mangoyi_Junior
