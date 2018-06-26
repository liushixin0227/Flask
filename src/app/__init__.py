#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 15:20
# @Author  : LiuShixin
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm
from flask import Flask

from src.app.models.book import db
from src.app.web import web


def create_app():
    app = Flask(__name__)
    app.config.from_object('src.app.config.secure')
    app.config.from_object('src.app.config.setting')
    app.register_blueprint(web)

    # db.init_app(app)
    # with app.app_context():
    #     db.create_all()
    return app

#
# def register_blueprint(app):
#     from src.app.web import web
#
#     app.register_blueprint(web)
