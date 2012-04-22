'''
Created on 21.4.2012

@author: teerytko
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_db_session(app):
    db_config = app.config['DATABASE_SETTINGS']
    engine = create_engine(app.config['DATABASE_ENGINE'],
                           **db_config)
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    app.config['DB_ENGINE'] = engine
    app.config['DB_SESSION'] = db_session
    Base.query = db_session.query_property()
    return db_session


def init_db(app):
    import models
    Base.metadata.create_all(bind=app.config['DB_ENGINE'])
    
def clear_db(app):
    Base.metadata.drop_all(bind=app.config['DB_ENGINE'])