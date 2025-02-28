#!/usr/bin/python3
"""This module defines a class User
Inherits from SQLAlchemy Base and links to the MySQL table users.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store users.
        email: (sqlalchemy String): The user's email address.
        password (sqlalchemy String): The user's password.
        first_name (sqlalchemy String): The user's first name.
        last_name (sqlalchemy String): The user's last name.
        places (sqlalchemy relationship): The User-Place relationship.
        reviews (sqlalchemy relationship): The User-Review relationship.
"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship('Place', backref='user', cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")

    def __init__(self, *args, **kwargs):
        """
        inherit from base  and Basemodel init
        """
        super().__init__(*args, **kwargs)
