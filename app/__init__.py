import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# Get the directory where the script is located. This is used to set up the database path.
basedir = os.path.abspath(os.path.dirname(__file__))

# Initialize the Flask application
app = Flask(__name__)

# Load configurations from the 'config' module inside the 'app' package.
app.config.from_object('app.config.Config')

# Initialize SQLAlchemy for database operations
db = SQLAlchemy()

# Initialize Bcrypt for password hashing
bc = Bcrypt(app)

# Initialize LoginManager for user authentication
lm = LoginManager()
lm.init_app(app)


# database setup
# @app.before_first_request
# def initialize_database():
#     db.create_all() depreciated

# Setup the database within the application context.
# This replaces the deprecated 'initialize_database' function, ensuring that the database is ready when the app starts.
with app.app_context():
    db.init_app(app)
    db.create_all()
    



# Import views and models from the 'app' package. 
# This is necessary to ensure that Flask knows about the routes and database models you've defined.
from app import views, models
