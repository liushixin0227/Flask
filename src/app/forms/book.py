#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 10:44
# @Author  : LiuShixin
# @Site    : 
# @File    : book.py
# @Software: PyCharm

from wtforms import Form, StringField, IntegerField
from wtforms.validators import NumberRange, Length, DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
