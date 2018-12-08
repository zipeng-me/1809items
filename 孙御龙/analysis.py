# -*- coding:utf-8 -*-
'''数据分析
实现：
    根据日线推算出12日的平均线。统计日线上穿12日线的次数sum，
    统计日线上穿12日线10个交易日后的仍然上涨的次数sec，
    模型概率cul=sec/sum，当概率大于0.80时，即可认为可靠性较高。（股票筛选）
	在上述筛选出的股票中，如果最近一次上穿至数据更新的最新时间，
    交易日间隔小于3日，即推荐买入。按照概率高低排序，从高到低选5支股票给客户。
反馈交易指导信息：
	接受用户反馈的股票编号，对该股票进行数据分析，将分析结果反馈给用户。
    概率小于0.80即不推荐买入。
    概率大于0.80但日期超过3天，即建议收藏，等待合适的买入时机。
    不超过3天但不在推荐的股票范围内，提示建议买入。
注：
    用函数或类封装方法，服务端启动时，循环调用方法对每只股票分析。
    用户指定股票，调用该方法对指定股票分析。
'''
import tushare

class Analysis(object):
    def __init__(self):
        self.get_stock_list()
        self.start()

    def start(self):
        # 记录符合条件的股票代码和比率
        stock_list = self.stock_list
        stock_check = []
        for code in stock_list:
            try:
                up, ten, days = self.analysis(code)
            except Exception:
                continue
            ratio = ten / up
            # 如果10天后上涨的次数与总次数的比率大于0.80，筛选
            if ratio >= 0.80 and days <= 3:
                stock_check.append((code, ratio))
            print(code, ratio, days, stock_check)
        print(stock_check)

    # 获取股票列表
    def get_stock_list(self):
        # 查询当前所有正常上市交易的股票列表
        data = tushare.get_stock_basics()
        self.stock_list = data.index

    # 分析
    def analysis(self, code):
        data_analysis = self.get_daydate(code)
        up_count, ten_count = self.count_avg_cross_day(data_analysis)
        up_days = self.count_up_last_days(data_analysis)
        return up_count, ten_count, up_days

    # 获取日线数据，元素形式[(日期, 收盘价, 12日均价),]
    def get_daydate(self, code):
        # 获取股票日线数据
        data_day = tushare.get_k_data(code)
        # 收盘价
        close = [close for close in data_day.close]
        # 获取12日均线
        data_12day = self.get_avgdata(close)
        # 提取数据，元素形式[(日期, 收盘价, 12日均价),]
        data_analysis = []
        for x in zip(data_day.date[13:], close[13:], data_12day):
            data_analysis.append(x)
        return data_analysis

    # 12天均线
    def get_avgdata(self, data):
        start = 0
        end = 13
        # 存放均线数据
        lst_temp = []
        while end <= len(data):
            data_sum = sum(data[start:end]) / 13
            lst_temp.append(data_sum)
            start += 1
            end += 1
        return lst_temp

    # 统计均线上穿次数和10天后股价仍高于日线的次数
    def count_avg_cross_day(self, data):
        # 上穿总次数
        count = 0
        # 上穿十天后仍高于日线的次数
        count_ten = 0
        i = 1
        while i < len(data):
            # 均线上穿日线
            if (data[i-1][2] < data[i-1][1]) & (data[i][2] > data[i][1]):
                count += 1
                # 10天后均线仍高于日线
                if data[i+10][2] > data[i+10][1]:
                    count_ten += 1
            i += 1
        return (count, count_ten)

    # 统计最后一次均线上穿日线距最后交易日的天数
    def count_up_last_days(self, data):
        # 记录天数
        count = 0
        i = -1
        while True:
            # 判断是否上穿
            if (data[i-1][2] < data[i-1][1]) & (data[i][2] > data[i][1]):
                break
            count += 1
            i -= 1
        return count

if __name__ == "__main__":
    a = Analysis()