#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.review import Review
from models.place import Place
import models
from os import getenv
import sqlalchemy


class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user")
    reviews = relationship("Review", backref="user")

    def __init__(self):
        self.email = ' '
        self.password = ' '
        self.first_name = ' '
        self.last_name = ' '
