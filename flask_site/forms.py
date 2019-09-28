from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

from flask_site.models import Book


class AddBookForm(FlaskForm):
    title = StringField(
        "Book Title", validators=[DataRequired(), Length(min=2, max=50)]
    )
    author = StringField("Author", validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField("Add the book!")
