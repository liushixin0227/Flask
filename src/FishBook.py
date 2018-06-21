#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 13:11
# @Author  : Aries
# @Site    : 
# @File    : FishBook.py
# @Software: PyCharm
import re

from src.app.libs.get_http import Http

from src.app.models.book import db


class FishBook(object):
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @staticmethod
    def check_the_repeat(isbn):
        items = list()
        sql = "SELECT * FROM books WHERE isbn = {}".format(isbn)
        items = list(db.session.execute(sql))
        return items

    @staticmethod
    def inser_table(book):
        sql = '''insert into books (title,author,binding,publisher,price,page,pubdata,isbn,summary,image ) VALUE ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(
            str(book['title']),
            re.findall("\'(.*)\'", str(book['author']))[0] if re.findall("\'(.*)\'", str(book['author'])) else '',
            str(book['binding']),
            str(book['publisher']), str(book['price']),
            book['pages'],
            str(book['pubdate']), str(book['isbn']), str(book['summary']), str(book['image']))
        db.session.execute(sql)

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = Http.get(url)
        return result



    @classmethod
    def search_by_keyword(cls, keyword, count=15, start=0):
        url = cls.keyword_url.format(keyword, count, start)
        result = Http.get(url)
        # for book in result['books']:
        #     if cls.check_the_repeat(book['isbn']) == []:
        #         cls.inser_table(book)
        return result
