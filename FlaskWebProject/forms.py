
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[DataRequired()])
    image_path = FileField('Image', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Save')

    def validate(self, extra_validators=None):
        initial_validation = super(PostForm, self).validate()
        if not initial_validation:
            return False

        # Additional custom validations
        if self.image_path.data:
            file = self.image_path.data
            if not file.filename.lower().endswith(('jpg', 'png')):
                self.image_path.errors.append("Only .jpg and .png files are allowed.")
                return False

        return True
