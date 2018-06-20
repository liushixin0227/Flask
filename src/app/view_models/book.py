#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/20 16:13
# @Author  : LiuShixin
# @Site    : 
# @File    : book.py
# @Software: PyCharm


class BookViewModels(object):

    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'book': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['book'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    @staticmethod
    def __cut_book_data(book):
        book = {
            'title': book['title'],
            'publisher': book['publisher'],
            'pages': book['pages'] or '',
            'price': book['price'],
            'author': book['author'],
            'summary': book['summary'] or '',
            'image': book['image'],

        }
        return book
