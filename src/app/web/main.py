#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 15:20
# @Author  : LiuShixin
# @Site    :
# @File    : __init__.py
# @Software: PyCharm
from . import web


@web.route('/')
def index():
    return 'This is index'


@web.route('/personal')
def personal_center():
    pass
