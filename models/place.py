#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import DateTime, Column, Integer, String,\
    Float, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id',
           String(60),
           ForeignKey('places.id'),
           primary_key=True,
           nullable=False),
    Column('amenity_id',
           String(60),
           ForeignKey('amenities.id'),
           primary_key=True,
           nullable=False))


class Place(BaseModel, Base):

    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place', cascade="delete")
        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            viewonly=False)

    else:
        @property
        def reviews(self):
            """Return list of review instances"""
            from models import storage
            rlist = []
            for k, v in storage.all(Review).items():
                if self.id == v.place_id:
                    rlist.append(v)
            return rlist

        @property
        def amenities(self):
            """List all amenities"""
            from models import storage
            from models.amenity import Amenity
            alist = []
            for k, v in storage.all(Amenity).items():
                if self.id == v.amenity_ids:
                    alist.append(v)
            return alist

        @amenities.setter
        def amenities(self, a):
            """Setter"""
            from models.amenity import Amenity
            if isinstance(a, Amenity):
                self.append(a)
