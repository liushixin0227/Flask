#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 15:20
# @Author  : LiuShixin
# @Site    :
# @File    : __init__.py
# @Software: PyCharm
from flask import current_app, flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from src.app import db
from src.app.models.gift import Gift
from src.app.view_models.gift import MyGifts
from . import web


@web.route('/my/gifts')
@login_required
def my_gifts():
    gifts_of_mine = Gift.get_user_gifts(current_user.id)
    isbn_list = [gift.isbn for gift in gifts_of_mine]
    wish_count_list = Gift.get_wish_count(isbn_list)
    view_model = MyGifts(gifts_of_mine, wish_count_list)
    return render_template('my_gifts.html', gifts=view_model.gifts)


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    # 捕捉数据库提交异常
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
    else:
        flash('这本书已经存在你的赠送清单或心愿单,请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
