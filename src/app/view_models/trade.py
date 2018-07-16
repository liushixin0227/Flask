#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/07/02 15:47
# @Author  : LiuShixin
# @Site    : 
# @File    : trade.py
# @Software: PyCharm
from src.app.view_models.book import BookViewModle


class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(single) for single in goods]

    def __map_to_trade(self, single):
        if single.create_datetime:
            time = single.create_datetime.strftime('%Y-%m-%d')
        else:
            time = '未知'
        return dict(
            user_name=single.user.nickname,
            time=time,
            id=single.id
        )


class MyTrades:
    def __init__(self, trade_of_mine, trade_count_list):
        self.trades = []
        self.__trade_of_mine = trade_of_mine
        self.__trade_count_list = trade_count_list
        self.trades = self.__parse()

    def __parse(self):
        trades = []
        for trade in self.__trade_of_mine:
            my_wish = self.__matching(trade)
            trades.append(my_wish)
        return trades

    def __matching(self, trade):
        count = 0
        for trade_count in self.__trade_count_list:
            if trade.isbn == trade_count['isbn']:
                count = trade_count['count']
        r = {
            'trades_count': count,
            'book': BookViewModle(trade.book),
            'id': trade.id
        }
        return r
