#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def is_isbn_or_key(work):
    index_type = 'key'
    short_work = work.replace('-', '')
    if (len(short_work) == 13 or len(short_work) == 10) and short_work.isdigit():
        index_type = 'isbn'
    return index_type
