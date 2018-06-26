#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 15:20
# @Author  : LiuShixin
# @Site    :
# @File    : __init__.py
# @Software: PyCharm

from . import web


@web.route('/my/wish')
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
def save_to_wish(isbn):
    pass


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
