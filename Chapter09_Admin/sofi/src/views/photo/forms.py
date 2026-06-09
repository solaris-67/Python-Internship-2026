from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed, FileSize
from wtforms.fields import StringField, DecimalField, SelectField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from string import ascii_uppercase, ascii_lowercase, digits, punctuation


class PhotoForm(FlaskForm):
    gmail = StringField('Your Gmail Address', validators=[DataRequired()])
    title = StringField('Photo Title', validators=[DataRequired()])
    artist = StringField('Name of the Artist', validators=[DataRequired()])
    category = SelectField('Category', coerce=int, validators=[DataRequired()])
    img = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], FileSize(1024 * 1024 * 5))])
    submit = SubmitField('Submit')


    def validate_password(self, field):
        has_lower = False
        has_upper = False
        has_digit = False
        has_punctuation = False

        for char in field.data:
            if char in ascii_lowercase:
                has_lower = True
            if char in ascii_uppercase:
                has_upper = True
            if char in digits:
                has_digit = True
            if char in punctuation:
                has_punctuation = True

        if not has_lower:
            raise ValidationError('Password requires lower case letters')

        if not has_upper:
            raise ValidationError('Password requires upper case letters')

        if not has_digit:
            raise ValidationError('Password requires digit')

        if not has_punctuation:
            raise ValidationError('Password requires punctuation')
