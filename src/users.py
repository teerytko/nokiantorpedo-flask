'''
Created on 21.4.2012

@author: teerytko
'''

from flask.views import MethodView

class UserAPI(MethodView):
    
    def get(self, user_id):
        if user_id is None:
            return "Users: %s" % []
        else:
            # expose a single user
            return "User: %s" % ''

    def post(self):
        # create a new user
        pass

    def delete(self, user_id):
        # delete a single user
        pass

    def put(self, user_id):
        # update a single user
        pass

