#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from models.city import City
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel, Base):
    """This is the class for state"""

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')

    def __init__(self, *args, **kwargs):
        """Inicialization inherited """
        super().__init__(*args, **kwargs)

    if models.storage_type != 'db':
        @property
        def cities(self):
            """Gets the list of City instances with state_id=State.id"""
            city_list = []
            all_city = models.storage.all(City)
            for value in all_city.values():
                if value.state_id == self.id:
                    city_list.append(value)
            return city_list
