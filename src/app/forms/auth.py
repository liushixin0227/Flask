#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/27 12:16
# @Author  : LiuShixin
# @Site    : 
# @File    : auth.py
# @Software: PyCharm
from wtforms import Form, StringField, PasswordField
from wtforms.validators import Length, DataRequired, Email, ValidationError, EqualTo

from src.app.models.user import User


class EmailForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])


class PassWordForm(EmailForm):
    password = PasswordField(validators=[DataRequired(message='密码不能为空,请输入密码'),
                                         Length(6, 32)])


class RegisterForm(PassWordForm):
    nickname = StringField(validators=[
        DataRequired(), Length(2, 10, message='昵称至少2个字符,最多10个字符')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已被注册')


class ResetPasswordForm(Form):
    password1 = PasswordField(validators=[
        DataRequired(),
        Length(6, 32, message='密码长度需要在6-32个字符之间'),
        EqualTo('password2', message='两次输入密码不相同')])

    password2 = PasswordField(validators=[DataRequired(),
                                          Length(6, 32)])
