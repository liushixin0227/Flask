#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 15:20
# @Author  : LiuShixin
# @Site    :
# @File    : __init__.py
# @Software: PyCharm
from flask import current_app, flash, redirect, url_for, render_template
from flask_login import current_user

from src.app import db
from src.app.models.wish import Wish
from src.app.view_models.trade import MyTrades
from src.app.view_models.wish import MyWishs
from . import web


@web.route('/my/wish')
def my_wish():
    wishs_of_mine = Wish.get_user_wishs(current_user.id)
    isbn_list = [gift.isbn for gift in wishs_of_mine]
    gift_count_list = Wish.get_gift_count(isbn_list)
    view_model = MyTrades(wishs_of_mine, gift_count_list)
    return render_template('my_wish.html', wishes=view_model.trades)


@web.route('/wish/book/<isbn>')
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            db.session.add(wish)
    else:
        flash('这本书已经存在你的赠送清单或心愿单,请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
