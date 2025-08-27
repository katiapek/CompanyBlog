# ourcompanyblog/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

db_file = os.getenv('SQLITE_DB')
db_path = os.path.join(basedir, db_file)

app = Flask(__name__)


#####################
# DATABASE SETUP ####
#####################
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

####################
# LOGIN CONFIGS ####
####################
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'


#####################
# Import Blueprints #
#####################
from ourcompanyblog.core.views import core
from ourcompanyblog.users.views import users
from ourcompanyblog.blog_posts.views import blog_posts
from ourcompanyblog.error_pages.handlers import error_pages
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)

#####################
# SECRET KEY ########
#####################
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')