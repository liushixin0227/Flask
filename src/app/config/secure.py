#!/usr/bin/env python
# _*_ coding:utf-8 _*_
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:pass@localhost:3306/flask_book'
SECRET_KEY = 'kDFy!AHo&rlq1Ir75@eE4!eeN$K*TWTH'
SQLALCHEMY_TRACK_MODIFICATIONS = True

#Email 配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = '522273565@qq.com'
MAIL_PASSWORD = 'zqfrdcamsmfobigg'
# MAIL_DEFAULT_SENDER : 默认为 None
# MAIL_MAX_EMAILS : 默认为 None
# MAIL_SUPPRESS_SEND : 默认为 app.testing
# MAIL_ASCII_ATTACHMENTS : 默认为 False
# MAIL_DEBUG : 默认为 app.debug
