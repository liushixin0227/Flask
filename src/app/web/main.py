#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 15:20
# @Author  : LiuShixin
# @Site    :
# @File    : __init__.py
# @Software: PyCharm
from flask import render_template

from src.app.models.gift import Gift
from src.app.view_models.book import BookViewModle
from . import web


@web.route('/')
def index():
    recent_gifts = Gift.rencent()
    books = [BookViewModle(gift.book) for gift in recent_gifts]
    return render_template('index.html', recent=books)


@web.route('/personal')
def personal_center():
    pass
