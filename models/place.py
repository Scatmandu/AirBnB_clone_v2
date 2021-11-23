#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import sqlalchemy
import os

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60), ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60), ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 backref="place_amenities", viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        '''init for place'''
        super().__init__(*args, **kwargs)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            '''getter for reviews'''
            reviewList = []
            allReviews = models.storage.all(Review)
            for review in allReviews.values():
                if review.place_id == self.id:
                    reviewList.append(review)
            return reviewList

        @property
        def amenities(self):
            '''getter for amenities'''
            amenityList = []
            allAmenities = models.storage.all(Amenity)
            for amenity in allAmenities.values():
                if amenity.place_id == self.id:
                    amenityList.append(amenity)
            return amenityList

        @amenities.setter
        def amenities(self, value):
            '''setter for amenity'''
            if isinstance(value, Amenity):
                self.append(value)
