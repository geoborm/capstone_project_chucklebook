from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TextAreaField
from wtforms.validators import InputRequired, EqualTo, Optional, URL

class SignUpForm(FlaskForm):
    full_name = StringField('Name', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Log In')

class ProfileForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    about_me = TextAreaField('Body', validators=[InputRequired()])
    image_url = StringField('Image URL')
    twitter_url = StringField('Twitter', validators=[Optional(), URL()])
    instagram_url = StringField('Instagram URL', validators=[Optional(), URL()])
    facebook_url = StringField('Facebook URL', validators=[Optional(), URL()])
    tiktok_url = StringField('Tik Tok URL', validators=[Optional(), URL()])
    youtube_url = StringField('YouTube URL', validators=[Optional(), URL()])
    submit = SubmitField('Create Profile')

