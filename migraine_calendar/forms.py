from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
import migraine_calendar.repository as repo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = repo.get_user_by_name(username.data)
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class MigraineForm(FlaskForm):
    start = DateField('Start', validators=[DataRequired()])
    stop = DateField('Stop')
    intensity = IntegerField('Intensity')
    medication = StringField('Medication')
    reason = StringField('Reason')
    notes = StringField('Notes')
    submit = SubmitField('Add')


class SleepForm(FlaskForm):
    start = DateField('Start', validators=[DataRequired()])
    stop = DateField('Stop')
    light_min = IntegerField('Light')
    deep_min = IntegerField('Deep')
    rem_min = IntegerField('Rem')
    awake_min = IntegerField('Awake')
    feeling = StringField('Feeling')
    notes = StringField('Notes')
    submit = SubmitField('Add')
