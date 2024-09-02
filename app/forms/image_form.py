from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField



ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "gif"}
# WTForm Class
class ImageForm(FlaskForm):
    image = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
