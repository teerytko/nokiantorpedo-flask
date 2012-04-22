'''
Created on 21.4.2012

@author: teerytko
'''

import json

from flask.views import MethodView
from flask import make_response, request, current_app
from models import User



def find_users_rest():
    """
    Find users with query params.
    """
    ret = []
    for user in find_users(**request.args.to_dict()):
        ret.append(user.to_dict())
    return make_response(json.dumps(ret))


def get_user(user_id):
    """
    Get a user by its id.
    """
    return User.query.filter(User.id == user_id).first()


def create_user(**data):
    """
    Create a user with given data
    """
    u = User(**data)
    db_session = current_app.config['DB_SESSION']
    db_session.add(u)
    return True


def delete_user(user_id):
    """
    Create a user with given data
    """
    u = get_user(user_id)
    db_session = current_app.config['DB_SESSION']
    db_session.delete(u)
    return True


def update_user(user_id, **data):
    """
    Create a user with given data
    """
    u = get_user(user_id)
    for key, value in data.items():
        setattr(u, key, value)
    return True


def find_users(**params):
    """
    Find users with query params
    @return: a list of users that match the params.
    """
    qitems = []
    for key, value in params.items():
        qitems.append("%s='%s'" % (key,value))
    query = ' and '.join(qitems)
    return User.query.filter(query)

class UserAPI(MethodView):
    def get(self, user_id):
        if user_id is None:
            ret = []
            for user in User.query.all():
                ret.append(user.to_dict())
            return make_response(json.dumps(ret))
        else:
            # expose a single user
            user = get_user(user_id)
            return make_response(json.dumps(user.to_dict()))

    def post(self):
        # create a new user
        data = request.form.to_dict(flat=True)
        success = create_user(**data)
        return json.dumps({'success': success})

    def delete(self, user_id):
        # delete a single user
        success = delete_user(user_id)
        return json.dumps({'success': success})

    def put(self, user_id):
        # update a single user
        data = request.form.to_dict(flat=True)
        success = update_user(user_id, **data)
        return json.dumps({'success': success})
