#coding:utf8

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,FileField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError
from app.models import Admin,Tag


tags = Tag.query.all()


class LoginForm(FlaskForm):
    account = StringField(
        label="account",
        validators= [
            DataRequired("Please input account name")
        ],
        description='account',
        render_kw={
            'class':'form-control',
            'placeholder':'Please input your account',
            'required':'required'
        }

    )

    pwd = PasswordField(
        label="pwd",
        validators=[
            DataRequired("Please input password")
        ],
        description='password',
        render_kw={
            'class': 'form-control',
            'placeholder': 'Please input your password',
            'required': 'required'
        }
    )

    submit = SubmitField(
        'Login',
        render_kw = {
            'class':'btn btn-primary btn-block btn-flat'
        }
    )


    def validate_account(self, field):
        account = field.data
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError('Account does not exist')


class TagForm(FlaskForm):
    name = StringField(
        label='name',
        validators= [
            DataRequired('Please input label!')
        ],
        description='Label',
        render_kw={
            'class':'form-control',
            'id':'input_name',
            'placeholder':'Please input label name'
        }
    )
    submit = SubmitField(
        'Edit',
        render_kw = {
            'class':'btn btn-primary'
        }
    )


class MovieForm(FlaskForm):
    title = StringField(
        label='title',
        validators=[
            DataRequired('Please input title!')
        ],
        description='Label',
        render_kw={
            'class': 'form-control',
            'id': 'input_title',
            'placeholder': 'Please input title'
        }
    )

    url = FileField(
        label= "file",
        validators=[
            DataRequired("please upload file")
        ],
        description='file'
    )


    info = TextAreaField(
        label='description',
        validators=[
            DataRequired('Please input description!')
        ],
        description='description',
        render_kw={
            'class': 'form-control',
            'rows' : 10
        }
    )

    logo = FileField(
        label="cover",
        validators=[
            DataRequired("please upload cover")
        ],
        description='cover'
    )

    star = SelectField(
        label = 'star',
        validators= [
            DataRequired("please select star")
        ],
        description='star',
        coerce=int,
        choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')],
        render_kw = {
        'class': 'form-control',
    }
    )

    tag_id = SelectField(
        label='tag',
        validators=[
            DataRequired("please select tag")
        ],
        description='tag',
        coerce=int,
        choices=[(v.id, v.name) for v in tags],
        render_kw={
            'class': 'form-control',
        }
    )

    area = StringField(
        label='area',
        validators= [
            DataRequired('Please input area!')
        ],
        description='Label',
        render_kw={
            'class':'form-control',
            'placeholder':'Please input area name'
        }
    )


    length = StringField(
        label='length',
        validators= [
            DataRequired('Please input length!')
        ],
        description='length',
        render_kw={
            'class':'form-control',
            'placeholder':'Please input length'
        }
    )

    release_time = StringField(
        label='upload time',
        validators= [
            DataRequired('Please input upload time!')
        ],
        description='upload time',
        render_kw={
            'class':'form-control',
            'placeholder':'Please input upload time',
            'id':'input_release_time'
        }
    )

    submit = SubmitField(
        'movieform',
        render_kw = {
            'class':'btn btn-primary'
        }
    )