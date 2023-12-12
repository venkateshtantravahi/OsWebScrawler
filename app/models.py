from app import db
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    """
    Represents a user in the application. This class is a model that defines the structure of the 'Users' table in the database.

    Attributes:
        id (int): Unique identifier for the user.
        firstname (str): First name of the user.
        lastname (str): Last name of the user.
        user (str): Username of the user.
        email (str): Email address of the user.
        password (str): Hashed password of the user.
        crawleddata (relationship): Relationship to the CrawledData model.
    """

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(60))
    lastname = db.Column(db.String(20))
    user = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(500))
    crawleddata = db.relationship('CrawledData', backref='user', lazy=True)

    def __init__(self, firstname, lastname, user, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.user = user
        self.email = email
        self.password = password

    def __repr__(self):
        return str(self.id) + ' - ' + str(self.user)

    def save(self):
        db.session.add(self)
        db.session.commit()

        return self
    

class CrawledData(db.Model):
    """
    Represents crawled data associated with a user. This class defines the structure of the 'CrawledData' table in the database.

    Attributes:
        id (int): Unique identifier for the crawled data.
        user_id (int): Foreign key to the Users table.
        url (str): URL of the crawled data.
        title (str): Title of the crawled page or data.
        content (str): Content extracted from the crawled page.
        file_path (str): File path where crawled data is stored (if applicable).
        content_type (str): Type of content crawled.
        links (PickleType): Serialized list of links found in the crawled content.
    """
    
    __tablename__ = 'CrawledData'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    url = db.Column(db.String(500), unique=True, nullable=False)
    title = db.Column(db.String(300), nullable=False)
    content = db.Column(db.Text, nullable=False)
    file_path = db.Column(db.String, nullable=True)
    content_type = db.Column(db.String, nullable=True)
    links = db.Column(db.PickleType, nullable=True)  # Storing list of links as serialized data

    def __init__(self, user_id, url, title, content,file_path, content_type, links):
        self.user_id = user_id
        self.url = url
        self.title = title
        self.content = content
        self.file_path = file_path
        self.content_type = content_type
        self.links = links
    
    def __repr__(self):
        return f"{self.id} - User: {self.user_id} - URL: {self.url}"
    
    def save(self):
        db.session.add(self) 
        print('added to db waiting to commit')
        db.session.commit()
        return self


    



class Data(db.Model):
    """
    Represents generic data stored in the application. This class is a model that defines the structure of the 'Data' table in the database.

    Attributes:
        id (int): Unique identifier for the data entry.
        version (str): Version of the data or related application component.
        status (str): Status associated with the data.
        error_code (int): Error code associated with the data, if applicable.
    """

    __tablename__ = 'Data'

    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.String(12), unique=True)
    status = db.Column(db.String(7))
    error_code = db.Column(db.Integer)

    def __init__(self, version, status, error_code):
        self.version = version
        self.status = status
        self.error_code = error_code
    
    def save(self):
        db.session.add(self)
        db.session.commit()

        return self