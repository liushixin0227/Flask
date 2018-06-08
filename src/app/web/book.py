#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 16:02
# @Author  : LiuShixin
# @Site    : 
# @File    : book.py
# @Software: PyCharm
from flask import jsonify, request
from src.FishBook import FishBook
from src.app.web import web
from src.helper import is_isbn_or_key


@web.route('/book/search')
def search():
    q = request.args['q']
    page = request.args['page']
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = FishBook.search_by_isbn(q)
    else:
        result = FishBook.search_by_keyword(q)
    return jsonify(result)

# app.add_url_rule('/first/', view_func=hello)
