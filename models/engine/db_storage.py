#!/usr/bin/python3
"""class file DBStorage"""

from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

import models
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State


class DBStorage:
    """the DBStorage class"""

    __engine = None
    __session = None
    all_classes = ["State", "City", "User", "Place", "Review"]

    def __init__(self):
        """initiate a dbstorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return a new dictionary with all objects depending
        of the class name"""
        new_dict = {}
        if cls is None:
            for class_name in self.all_classes:
                cls = getattr(models, class_name)
                for instance in self.__session.query(cls).all():
                    key = instance.__class__.__name__ + '.' + instance.id
                    new_dict[key] = instance
        else:
            for instance in self.__session.query(cls).all():
                key = instance.__class__.__name__ + '.' + instance.id
                new_dict[key] = instance
        return new_dict

    def new(self, obj):
        """adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and the current
        database session"""
        Base.metadata.create_all(self.__engine)
        session_db = sessionmaker(bind=self.__engine,
                                  expire_on_commit=False)
        self.__session = scoped_session(session_db)

    def close(self):
        """remove method: remove the session"""
        self.__session.close()
