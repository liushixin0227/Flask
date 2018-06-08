#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 15:20
# @Author  : LiuShixin
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from src.app.web import web

    app.register_blueprint(web)
