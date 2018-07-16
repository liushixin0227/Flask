#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/07/16 10:55
# @Author  : LiuShixin
# @Site    : 
# @File    : mail.py
# @Software: PyCharm
from flask import current_app, render_template

from src.app import mail
from flask_mail import Message


def send_mail(to_user, subject, template, **kwargs):
    msg = Message('[鱼书]' + ' ' + subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to_user])
    msg.html = render_template(template, **kwargs)
    mail.send(msg)
