'''
Created on 21.4.2012

@author: teerytko
'''


from flask import Flask
from flask import render_template, request, flash, redirect, url_for
from flaskext.login import LoginManager, login_user, login_required

from utils import register_api
from rest.users import UserAPI, get_user, create_user, find_users, \
find_users_rest
from database import init_db, create_db_session, clear_db
from forms import RegistrationForm, LoginForm

login_manager = LoginManager()


def create_userapp(config):
    app = Flask(__name__)
    app.config.from_object(config)
    create_db_session(app)
    login_manager.setup_app(app)
    register_urls(app)
    app.init_db = lambda : init_db(app)
    app.clear_db = lambda : clear_db(app)
    return app

def register_urls(app):
    # register REST interfaces
    register_api(app, UserAPI, 'user_api', '/users/', pk='user_id')
    app.add_url_rule('/users/find', 'find_users_rest', find_users_rest, methods=['GET'])
    

    @login_manager.user_loader
    def load_user(userid):
        return get_user(userid)

    @app.route("/login", methods=["GET", "POST"])
    def login():
        form = LoginForm(request.form)
        if request.method == 'POST' and form.validate():
            # login and validate the user...
            try:
                user = find_users(name=form.username.data)[0]
                if user.password == form.password.data:
                    login_user(user)
                    flash("Logged in successfully.")
                    return redirect(request.args.get("next") or url_for("index"))
            except IndexError:
                # user not found
                pass
        return render_template("login.html", form=form)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        app.logger.info("register")
        form = RegistrationForm(request.form)
        if request.method == 'POST' and form.validate():
            success = create_user(name=form.username.data, 
                        email=form.email.data,
                        password=form.password.data)
            if success:
                flash('Thanks for registering')
                return redirect(url_for('login'))
        return render_template('register.html', form=form)

    @app.route("/")
    def index():
        app.logger.info("test index")
        return render_template('main.html')
    
    @app.route("/hello/")
    @app.route("/hello/<username>")
    @login_required
    def hello(username=None):
        return render_template('hello.html', name=username)

    @app.teardown_request
    def shutdown_session(exception=None):
        db_session = app.config['DB_SESSION']
        db_session.commit()
        db_session.remove()
