#!/usr/bin/python3
'''This modules defines DBStorage class'''

from models.base_model import BaseModel, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    '''Defining class Storage'''

    __engine = None
    __session = None

    def __init__(self):
        '''Init for class DBstorage'''
        USER = getenv('HBNB_MYSQL_USER')
        PWD = getenv('HBNB_MYSQL_PWD')
        HOST = getenv('HBNB_MYSQL_HOST')
        DB = getenv('HBNB_MYSQL_DB')
        ENV = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            USER, PWD, HOST, DB, ENV), pool_pre_ping=True)

        if ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Method to retrieve all objects depending of the class name"""
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.base_model import BaseModel
        from models.state import State
        from models.review import Review
        from models.amenity import Amenity

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        if cls:
            newDict = {}
            allClassObjs = self.__session.query(cls).all()
            for obj in allClassObjs:
                key = type(obj).__name__ + "." + obj.id
                newDict[key] = obj
            return (newDict)
        else:
            allDicts = {}

            dictList = []
            State = self.all('State')
            City = self.all('City')
            Place = self.all('Place')
            Review = self.all('Review')
            User = self.all('User')
            Amenity = self.all('Amenity')
            dictList.append(State)
            dictList.append(City)
            dictList.append(Place)
            dictList.append(Review)
            dictList.append(User)
            dictList.append(Amenity)

            for dicts in dictList:
                allDicts.update(dicts)

            return(allDicts)

    def new(self, obj):
        '''new obj for sql'''
        self.__session.add(obj)

    def save(self):
        '''saves through commit to db'''
        self.__session.commit()

    def delete(self, obj=None):
        '''deletes an obj'''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.base_model import BaseModel
        from models.state import State
        from models.review import Review
        from models.amenity import Amenity
        '''reloads db'''
        Base.metadata.create_all(self.__engine)

        sessionFactory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)

        Session = scoped_session(sessionFactory)
        self.__session = Session()

    def close(self):
        '''close method for session'''
        self.__session.close()
