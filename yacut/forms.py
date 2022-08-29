from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField


class ShortURLForm(FlaskForm):
    original_link = URLField()
    custom_id = StringField()
    submit = SubmitField("Создать")
