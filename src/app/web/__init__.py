#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 15:23
# @Author  : LiuShixin
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm
from flask import Blueprint

web = Blueprint('web', __name__)
from . import book
# from . import user
