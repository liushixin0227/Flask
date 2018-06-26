#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 15:20
# @Author  : LiuShixin
# @Site    :
# @File    : __init__.py
# @Software: PyCharm
from . import web


@web.route('/my/gifts')
def my_gifts():
    pass


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
