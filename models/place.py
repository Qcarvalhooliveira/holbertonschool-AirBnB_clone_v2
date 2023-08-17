#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from os import getenv
from sqlalchemy.orm import relationship
import models

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             nullable=False, primary_key=True),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             nullable=False, primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)

        amenities = relationship("Amenity", secondary='place_amenity',
                                 viewonly=False)

        reviews = relationship("Review", cascade="all, delete",
                               backref="place")

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        numbe_rooms = 0
        number_bathrooms = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """returns the list of Review"""
            new = []
            for element in models.storage.all(Review):
                if element.place_id == self.id:
                    new.append(element)
            return new

        @property
        def amenities(self):
            """returns the list of amenities"""
            new = []
            for element in models.storage.all(Amenity):
                if new.id == self.amenity_ids:
                    new.append(element)
            return new

        @amenities.setter
        def amenities(self, obj):
            """Setter for amenities Object"""
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
