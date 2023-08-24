#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
import models
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime,
                        nullable=False,
                        default=datetime.utcnow()
                        )
    updated_at = Column(DateTime,
                        default=datetime.utcnow(),
                        nullable=False
                        )
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        if kwargs:
            for key, vle in kwargs.items():
                if key in ("created_at", "updated_at"):
                    vle = datetime.strptime(vle, "%Y-%m-%dT%H:%M:%S.%f")
                if "__class__" not in key:
                    setattr(self, key, vle)

    def __str__(self):
        """Updates updated_at with current time when instance is changed"""
        dictt = self.to_dict()
        cls = str(type(self)).split('.')[-1].split('\'')[0]
        return "[{:s}] ({:s}) {}".format(cls, self.id,
                                         dictt)

    def save(self):
        """
            Updates updated_at with current time when instance is changed
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dic = {}
        dic.update(self.__dict__)
        try:
            del dic['_sa_instance_state']
        except Exception:
            pass
        dic.update({'__class__':
                               (str(type(self)).split('.')[-1]).split('\'')[0]})
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()

        return dic

    def delete(self):
        """
            delete object
        """
        models.storage.delete(self)
