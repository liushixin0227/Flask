#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 16:02
# @Author  : LiuShixin
# @Site    : 
# @File    : book.py
# @Software: PyCharm
import json

from flask import jsonify, request, render_template, flash
from src.app.spider.FishBook import FishBook
from src.app.forms.book import SearchForm
from src.app.view_models.book import BookCollection
from src.app.web import web
from src.app.libs.helper import is_isbn_or_key


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    pass


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
