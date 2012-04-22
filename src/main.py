'''
Created on 21.4.2012

@author: teerytko
'''

from userapp import create_userapp


if __name__ == "__main__":
    print "starting main"
    app = create_userapp('settings.DefaultConfig')
    app.run(debug=app.config['DEBUG']
            )
