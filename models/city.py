#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.place import Place
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(128), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", backref="cities", cascade='delete')

    def __init__(self, *args, **kwargs):
        """Initialization inherited"""
        super().__init__(*args, **kwargs)
