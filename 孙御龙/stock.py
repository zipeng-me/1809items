# -*- coding:utf-8 -*-
'''股票
股票功能：
aaaa
'''
import tushare
import pymysql
from server import Server

class Stock(Server):
    # 初始化
    def __init__(self):
        # 生成数据库游标，可以直接用self.cur调用
        self.database('localhost', 'root', '123456', 'test', 3306, 'utf8')

    # 获取股票数据
    def get_stock_data(self):
        pass

    # 将股票数据写入数据库
    def write_to_db(self):
        pass

    # 获取股票列表
    def get_stock_list(self):
        pass

    # 画k线
    def draw_k(self, code):
        pass

    