'''
Created on 21.4.2012

@author: teerytko
'''

# configuration
class DefaultConfig(object):
    DATABASE_ENGINE = 'sqlite:///test.db'
    DATABASE_SETTINGS = {'echo': False,
                         'convert_unicode': True
                         }
    DEBUG = True
    USE_RELOADER = False
    USE_DEBUGGER = False
    SECRET_KEY = 'development key'
