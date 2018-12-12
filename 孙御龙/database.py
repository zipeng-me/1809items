# -*- coding:utf-8 -*-
'''数据库操作

'''
import pymysql
import os, sys
import stock
import time

class Database(object):
    # 初始化
    def __init__(self, host='localhost', user='root', 
    password='123456', database='stock', port=3306, charset='utf8'):
        self.DB_HOST = host
        self.DB_USER = user
        self.DB_PORT = port
        self.DB_PASSWD = password
        self.DB_NAME = database
        self.DB_CHARSET = charset
        # 建立游标对象
        self.cur = self.get_cur()

    # 获取数据库游标
    def get_cur(self):
        # 建立数据连接
        self.db = pymysql.connect(
            host = self.DB_HOST,
            user = self.DB_USER,
            password = self.DB_PASSWD,
            database = self.DB_NAME,
            charset = self.DB_CHARSET,
            port = self.DB_PORT)
        # 返回数据库游标对象
        return self.db.cursor()

    # 数据库交互
    def commit_to_database(self, sql):
        try:
            self.cur.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()

    # 关闭数据库
    def close_database(self):
        self.db.close()
    
    # 建立股票表data_day
    def create_stock_table(self):
        '''创建股票表
        表名为data_day
        '''
        sql = '''create table data_day(
              id int primary key auto_increment,
              date varchar(11) not null,
              code varchar(11) not null,
              open float(7,2) not null,
              close float(7,2) not null,
              hign float(7,2) not null,
              low float(7,2) not null,
              ma5 float(7,2) not null,
              ma10 float(7,2) not null,
              ma20 float(7,2) not null
              )engine=innodb, charset=utf8'''
        self.commit_to_database(sql)
    
    # 插入股票数据data_day
    def insert_stock_table(self, *args):
        sql = 'insert into data_day values(0, %r, %r, %f, %f, %f, %f, %f, %f, %f)' % args[0]
        self.commit_to_database(sql)

    # 给股票数据添加索引(code)
    def set_index_on_stock(self):
        sql = "alter table data_day add index code_index(code)"
        self.commit_to_database(sql)

    # 从股票数据库中查询数据
    def select_stock_table(self, code, tablename, *args):
        '''根据参数查询数据
        code:股票编号，字符串
        tablename:数据表名称，字符串
        *args:字符串元祖或列表，元素为要查询的数据
        例：
        select_stock_table('600660', 'data_day', ('code', 'open', 'close'))
        如果查询错误，返回-1
        '''
        s = ','.join(args[0])   
        sql = "select %s from %s where code=%r" % (s, tablename, code)
        try:
            self.cur.execute(sql)
        except Exception:
            return -1

    # 读取数据库查询数据
    def fetch_data(self):
        return self.cur.fetchall()

    # 将所有股票数据导入数据库data_day
    def write_all_stock_data(self):
        # 创建股票对象
        s = stock.Stock()
        # 获取所有正常交易的股票列表
        code_lst = s.getStockList()
        for code in code_lst:
            try:
                # 获取股票的所有日线数据
                lst = s.getStockHistData(code)
            except Exception:
                # 如果加载不成功，继续向后加载
                continue
            for x in lst:
                # 将数据写入数据库
                self.insert_stock_table(x)
        return 1
    
    # 创建用户信息表userinfo
    def create_userinfo_table(self):
        sql = '''create table userinfo(
              id int not null primary key auto_increment,
              name varchar(30) not null,
              password varchar(15) not null,
              unique(name))engine=innodb, charset=utf8'''
        self.commit_to_database(sql)

    # 向用户信息表userinfo中插入数据
    def insert_userinfo_table(self, name, password):
        sql = "insert into userinfo values(0, %r, %r)" % (name, password)
        self.commit_to_database(sql)

    # 查询用户信息表userinfo的数据
    def select_userinfo_table(self, name, password):
        sql = "select name,password from userinfo where name=%r and password=%r" % (name, password)
        try:
            self.cur.execute(sql)
        except Exception:
            return -1

    # 创建推送信息表stockinfo
    def create_stockinfo_table(self):
        sql = '''create table stockinfo(
              id int not null primary key auto_increment,
              date varchar(11) not null,
              code varchar(11) not null,
              up_count float(7,2) not null,
              ten_count float(7,2) not null,
              ratio float(7,2) not null,
              days int not null,
              content text not null
              )engine=innodb, charset=utf8'''
        self.commit_to_database(sql)
    
    # 向推送信息表stockinfo中插入数据
    def insert_stockinfo_table(self, *args):
        '''在推送信息表stockinfo中插入数据
        接收列表或元祖
        '''
        sql = "insert into stockinfo values(0, %r, %r, %f, %f, %f, %d, %r)" % args[0]
        self.commit_to_database(sql)

    # 查询stockinfo中的数据
    def select_stockinfo_table(self, code, date=str(time.strftime('%Y-%m-%d',time.localtime()))):
        '''查询股票推送信息
        code:股票编码，字符串
        date:日期，字符串，默认为当前日期
        查询失败返回-1
        '''
        sql = "select content from stockinfo where code=%r and date=%r" % (code, date)
        try:
            self.cur.execute(sql)
        except Exception:
            return -1
    
    # 

if __name__ == "__main__":
    d = Database()
    # sql = d.create_stock_table()
    s = stock.Stock()
    # lst = s.getStockHistData()
    # for x in lst:
    #     d.insert_stock_table(x)
    # print('提交成功')
    # d.set_index_on_stock()
    # d.select_stock_table('600660', 'data_day', ('code', 'open', 'close'))
    # print(d.fetch_data())
    # code_lst = s.getStockList()
    # for code in code_lst:
    #     try:
    #         lst = s.getStockHistData(code)
    #     except Exception:
    #         print(code, '未成功加载')
    #         continue
    #     for x in lst:
    #         d.insert_stock_table(x)
    #     print(code)
    # d.create_userinfo_table()
    d.create_stockinfo_table()
    # d.close_database()