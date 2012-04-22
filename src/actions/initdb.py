'''
Created on 6.5.2012

@author: teerytko
'''


from userapp import create_userapp
from database import init_db

if __name__ == "__main__":
    app = create_userapp('settings.DefaultConfig')
    app.config['DATABASE_SETTINGS']['echo'] = True
    print "Creating database %r" % app.config['DATABASE_ENGINE']
    init_db(app)
