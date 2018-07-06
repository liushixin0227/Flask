#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 12:37
# @Author  : LiuShixin
# @Site    : 
# @File    : get_http.py
# @Software: PyCharm

import requests


class Http(object):
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
