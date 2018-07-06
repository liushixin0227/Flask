#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 16:02
# @Author  : LiuShixin
# @Site    : 
# @File    : book.py
# @Software: PyCharm

from flask import request, render_template, flash
from flask_login import current_user

from src.app.forms.book import SearchForm
from src.app.models.gift import Gift
from src.app.models.wish import Wish
from src.app.spider.FishBook import FishBook
from src.app.view_models.book import BookCollection, BookViewModle
from src.app.view_models.trade import TradeInfo
from src.app.web import web
from src.app.libs.helper import is_isbn_or_key


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    # 默认当前登录用户没有赠送/心愿书籍
    has_in_gift = False
    has_in_wishes = False

    # 获取书籍详情数据
    fishbook = FishBook()
    fishbook.search_by_isbn(isbn)
    book = BookViewModle(fishbook.first)

    # current_user.is_authenticated判断用户是否登录,然后判断当前登录用户的清单
    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_gift = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_wishes = True

    # 从数据库获取赠送/心愿清单
    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    # 格式化心愿/赠送清单数据
    trade_wishes_model = TradeInfo(trade_wishes)
    trade_gifts_model = TradeInfo(trade_gifts)

    return render_template('book_detail.html', book=book,
                           wishes=trade_wishes_model, gifts=trade_gifts_model,
                           has_in_gift=has_in_gift, has_in_wishes=has_in_wishes)


@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        fishbook = FishBook()
        if isbn_or_key == 'isbn':
            fishbook.search_by_isbn(q)
        else:
            fishbook.search_by_keyword(q, page)
        books.fill(fishbook, q)
    else:
        flash('搜索关键字不符合要求,请重新输入关键字')
    return render_template('search_result.html', books=books)
# app.add_url_rule('/first/', view_func=hello)
