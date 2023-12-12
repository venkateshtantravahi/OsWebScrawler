import os
from decouple import config
import redis

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Configuration class for the Flask application.

    This class contains settings and configurations used by the Flask application, such as secret keys, 
    database connection details, and other related settings.

    Attributes:
    SECRET_KEY (str): A secret key used for securely signing the session cookie in Flask. 
                      It can be set from environment variables using 'decouple.config'.
                      Defaults to 's4cret_123' if not set in the environment.
    SQLALCHEMY_DATABASE_URI (str): Database URI for SQLAlchemy. Points to a SQLite database in the project directory.
    SQLALCHEMY_TRACK_MODIFICATIONS (bool): Flag to enable or disable track modifications feature in SQLAlchemy. 
                                           Set to False to disable it and improve performance.
    redis_host (str): Host address for the Redis server. Replace with the actual IP address or hostname.
    redis_port (int): Port number for the Redis server.
    r (redis.Redis): Redis client instance, connected to the specified host and port.

    The configurations can be adjusted according to the deployment requirements of the application.
    """
    # CSRF_ENABLED = True
    # set up a secretkey/passcode
    SECRET_KEY = config('SECRET_KEY', default='s4cret_123')

    # db URI
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    redis_host = "172.28.9.74"  # Replace with the actual IP address
    redis_port = 6379
    r = redis.Redis(host=redis_host, port=redis_port)

    
