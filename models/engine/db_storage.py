#!/usr/bin/python3
"""
model to mange DB storage using sqlAlchemy
"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import sqlalchemy


class DBStorage:
    """
        This class manage DB storage for AirBnb
        Clone using sqlAlchemy
    """
    __engine = None
    __session = None
    all_classes = ["State", "City", "User", "Place", "Review"]

    def __init__(self):
        """
            Init __engine based on the Enviroment
        """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session (self.__session)
        all objects depending of the class name"""
        da = {}
        if cls is None:
            for cl in self.all_classes:
                cl = eval(cl)
                for instance in self.__session.query(cl).all():
                    key = instance.__class__.__name__ + '.' + instance.id
                    da[key] = instance
        else:
            for instance in self.__session.query(cls).all():
                key = instance.__class__.__name__ + '.' + instance.id
                da[key] = instance
        return da

    def new(self, obj):
        """
            Creating new instance in db storage
        """
        self.__session.add(obj)

    def save(self):
        """
            save changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
            Delete obj from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
            create table in database
        """
        Base.metadata.create_all(self.__engine)
        sesn_db = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sesn_db)
        self.__session = Session()

    def close(self):
        """
            calls remove()
        """
        self.reload()
        self.__session.close()
