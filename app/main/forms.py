from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FloatField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Length
import sqlalchemy as sa
from flask_babel import _, lazy_gettext as _l
from app import db
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'),
                             validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = db.session.scalar(sa.select(User).where(
                User.username == self.username.data))
            if user is not None:
                raise ValidationError(_('Please use a different username.'))


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something'), validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l('Submit'))


'''

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    book_title: so.Mapped[str] = so.mapped_column(sa.String(140))
    author: so.Mapped[str] = so.mapped_column(sa.String(140))
    author2: so.Mapped[str] = so.mapped_column(sa.String(140))
    price: so.Mapped[float] = so.mapped_column(sa.Float)
    language: so.Mapped[str] = so.mapped_column(sa.String(140))
    category: so.Mapped[str] = so.mapped_column(sa.String(140))
    total_cnt: so.Mapped[int] = so.mapped_column(sa.Integer, default=1)
    borrow_out_cnt: so.Mapped[int] = so.mapped_column(sa.Integer, default=0)
'''

class BookForm(FlaskForm):
    book_title = TextAreaField(_l('book title'), validators=[ DataRequired(), Length(min=1, max=140)])
    author = TextAreaField(_l('book author'), validators=[ DataRequired(), Length(min=1, max=140)])
    author2 = TextAreaField(_l('book authors if ther are any'))
    price = FloatField(validators=[DataRequired()])
    language = TextAreaField(_l('language'), validators=[ DataRequired(), Length(min=1, max=40)])
    category = TextAreaField(_l('catergory'), validators=[ DataRequired(), Length(min=1, max=40)])
    copies = IntegerField(validators=[DataRequired()])
    submit = SubmitField(_l('Add'))


class LoadBookInventoryForm(FlaskForm):
    submit = SubmitField(_l('Load Book Inventory'))


class SearchForm(FlaskForm):
    q = StringField(_l('Search'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'meta' not in kwargs:
            kwargs['meta'] = {'csrf': False}
        super(SearchForm, self).__init__(*args, **kwargs)


class MessageForm(FlaskForm):
    message = TextAreaField(_l('Message'), validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l('Submit'))
