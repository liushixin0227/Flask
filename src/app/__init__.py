#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 15:20
# @Author  : LiuShixin
# @Site    :
# @File    : __init__.py
# @Software: PyCharm
from flask import Flask

from src.app.models.base import db
from flask_login import LoginManager

login_manager = LoginManager()


# 将蓝图注册到核心对象app上
def register_web_blueprint(app):
    from src.app.web import web
    app.register_blueprint(web)


def create_app():
    app = Flask(__name__)
    app.config.from_object('src.app.config.secure')
    app.config.from_object('src.app.config.setting')
    register_web_blueprint(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
