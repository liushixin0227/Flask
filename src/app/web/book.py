#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 16:02
# @Author  : LiuShixin
# @Site    : 
# @File    : book.py
# @Software: PyCharm
from flask import jsonify, request
from src.app.spider.FishBook import FishBook
from src.app.forms.book import SearchForm
from src.app.view_models.book import BookViewModels
from src.app.web import web
from src.app.libs.helper import is_isbn_or_key


@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = FishBook.search_by_isbn(q)
            result = BookViewModels.package_single(result, q)
        else:
            result = FishBook.search_by_keyword(q, page)
            result = BookViewModels.package_collection(result, q)
        return jsonify(result)
    else:
        return jsonify(form.errors)
# app.add_url_rule('/first/', view_func=hello)
