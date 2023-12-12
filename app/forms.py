from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import Email, DataRequired


class LoginForm(FlaskForm):
    """
    Form for user login.

    This form is used to authenticate users in the application. It includes fields for the username, password, 
    and a 'remember me' option for sessions.

    Fields:
    username (StringField): Input field for the user's username. Validation requires the field to be filled (DataRequired).
    password (PasswordField): Input field for the user's password. Validation requires the field to be filled (DataRequired).
    remember (BooleanField): Checkbox to remember the user's login session.
    """
    username = StringField(u'Username', validators=[DataRequired()])
    password = PasswordField(u'Password', validators=[DataRequired()])
    remember = BooleanField(u'RememberMe')


class RegisterForm(FlaskForm):
    """
    Form for user registration.

    This form is used for registering new users in the application. It includes fields for the user's first name, 
    last name, username, password, and email address.

    Fields:
    firstname (StringField): Input field for the user's first name. Validation requires the field to be filled (DataRequired).
    lastname (StringField): Input field for the user's last name. Validation requires the field to be filled (DataRequired).
    username (StringField): Input field for the user's chosen username. Validation requires the field to be filled (DataRequired).
    password (PasswordField): Input field for the user's chosen password. Validation requires the field to be filled (DataRequired).
    email (StringField): Input field for the user's email address. Validation requires the field to be filled (DataRequired) and to contain a valid email address (Email).
    """
    firstname = StringField(u'FirstName', validators=[DataRequired()])
    lastname = StringField(u'LastName', validators=[DataRequired()])
    username = StringField(u'Username', validators=[DataRequired()])
    password = PasswordField(u'Username', validators=[DataRequired()])
    email = StringField(u'Email', validators=[DataRequired(), Email()])

