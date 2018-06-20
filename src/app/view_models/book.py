#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/15 18:31
# @Author  : LiuShixin
# @Site    : 
# @File    : book.py
# @Software: PyCharm
class BookViewModle():
    @classmethod
    def pacage_single(cls, data, keyword):
        returned = {
            'books': [],
            'title': 0,
            'keyword': keyword
        }
        if data:
            returned['title'] = 1
            returned['books'] = [cls.__cut_bool_data(data)]
        return returned

    @classmethod
    def pacage_colletion(cls, data, keyword):
        returned = {
            'books': [],
            'title': 0,
            'keyword': keyword
        }
        if data:
            returned['title'] = data['total']
            returned['books'] = [cls.__cut_bool_data(book) for book in data['books']]
            return returned

    @staticmethod
    def __cut_bool_data(data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book
