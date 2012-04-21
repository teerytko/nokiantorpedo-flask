'''
Created on 21.4.2012

@author: teerytko
'''

from flask import Flask
from flask import render_template

from database import db_session, init_db
from utils import register_api
from users import UserAPI

app = Flask(__name__)

@app.route("/")
def index():
    return "I am index!"

@app.route("/hello/")
@app.route("/hello/<username>")
def hello(username=None):
    return render_template('hello.html', name=username)

@app.route("/init/")
def init():
    init_db()
    return "success" 

# register REST interfaces
register_api(app, UserAPI, 'user_api', '/users/', pk='user_id')


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == "__main__":
    app.run(debug=True)
