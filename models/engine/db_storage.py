#!/usr/bin/python3
"""Storage engine for database
"""


import models
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.user import User
from models.review import Review
from models.place import Place
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv


classes = {
    "Amenity": Amenity,
    "City": City,
    "User": User,
    "State": State,
    "Place": Place,
    "Review": Review}


class DBStorage:

    """Database Storage
    """
    __engine = None
    __session = None

    def __init__(self):
        """Constructor for DB storage engine
        """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')))

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Display all objects
        """
        all_dict = {}
        if cls in classes:
            item = self.__session.query(classes[cls]).all()
            for obj in item:
                k = "{}.{}".format(obj.__class__.__name__, obj.id)
                v = obj
                all_dict[k] = v
        elif cls is None:
            for model in classes:
                item = self.__session.query(classes[cls]).all()
                for obj in item:
                    k = "{}.{}".format(obj.__class__.__name__, obj.id)
                    v = obj
                    all_dict[k] = v
        return all_dict

    def new(self, obj):
        """add object to current database session
        """
        self.__session.add(obj)

    def save(self):
        """Commit changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from database
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Magic
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session()

    def close(self):
        """Close session"""
        self.__session.close()
