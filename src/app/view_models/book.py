#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/20 16:13
# @Author  : LiuShixin
# @Site    : 
# @File    : book.py
# @Software: PyCharm


class BookViewModle(object):
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = '、'.join(book['author'])
        self.image = book['image']
        self.isbn = book['isbn']
        self.price = book['price']
        self.summary = book['summary'] or ''
        self.pages = book['pages'] or ''

    @property
    def intro(self):
        inters = filter(lambda x: True if x else False, [self.author, self.publisher, self.price])
        return '/'.join(inters)


class BookCollection(object):
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, FishBook, keyword):
        self.total = FishBook.total
        self.keyword = keyword
        self.books = [BookViewModle(book) for book in FishBook.books]
