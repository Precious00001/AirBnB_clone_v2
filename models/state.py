#!/usr/bin/python3
"""State Module for HBNB project"""
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='delete', backref="state")

    @property
    def cities(self):
        var = models.storage.all()
        li = []
        list_city = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                li.append(var[key])
        for elem in li:
            if (elem.state_id == self.id):
                list_city.append(elem)
        return (list_city)
