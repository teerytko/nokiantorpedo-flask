'''
Created on 21.4.2012

@author: teerytko
'''

from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')

    def __repr__(self):
        return '<User %r>' % (self.name)

    def to_dict(self):
        return {'id': self.id,
                'name': self.name,
                'email': self.email,
                'password': self.password,
                }

    def is_active(self):
        return True 

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False