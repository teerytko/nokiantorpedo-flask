'''
Created on 6.5.2012

@author: teerytko
'''


from userapp import create_userapp
from database import clear_db

if __name__ == "__main__":
    app = create_userapp('settings.DefaultConfig')
    print "Cleaning database %r" % app.config['DATABASE_ENGINE']
    clear_db(app)
