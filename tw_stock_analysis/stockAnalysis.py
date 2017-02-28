# -*- coding: utf-8 -*-
from Models.stock import YCStock
import json
import logging
import math
from logging.config import fileConfig

logger = logging.getLogger(__name__)

AVERAGE_DAY_FOR_SEASON = 90
MA_5 = 5
MA_10 = 10
ACCEPTABLE_PERCENTAGE = 0.03

class StockAnalysis(object):
    """藏股分析買點"""
    def analysis(self):
        print '開始分析'
        print '傳入%d個參數' % len(self._stocks)
        for i in range(1, AVERAGE_DAY_FOR_SEASON):
            print "第%d次" % i
            if self.is_nothigh_averageup_valuedown_pricesame(i):
                print '分析到高點'
        
    def is_nothigh_averageup_valuedown_pricesame(self, index = 1):
        """股價不在高點 ＆ 三日線呈現上漲 & 量縮 ＆ 價平 => 漲很大"""
        result = True
        lastStcok = self._stocks[-index]
        
        """股價不在高點 ＆ 三日線呈現上漲 & 量縮 ＆ 價平 => 漲很大"""
        # 先計算目前股價是否在高點
        # 計算五日均價與持續天數 MA5
        get_higher_point = self.__get_higher_point(self._grs_stock.price, index)
        logging.debug('成交價：%.3f' % lastStcok.close_price)
        logging.debug('高點 %.2f ' % get_higher_point)
        result &= get_higher_point <= lastStcok.close_price

        # 三日線呈現上漲
        ma, cont_days = self._grs_stock.MA(MA_5)
        logging.debug('均價：%.3f' % ma[-index])
        cont_days = self.cal_continue(ma[0: -index])
        result &= (cont_days > 0 and cont_days < MA_5)

        # 量縮
        temp, v1 = self.__how_variety_volumn(index)
        result &= temp < 0

        # 價平
        temp, v2 = self.__how_variety_close_price(index)
        result &= temp == 0

        if result: 
            logging.info('%s-%s 買點!!!',lastStcok.stockno, lastStcok.date)
            logging.info('量: %f', v1)
            logging.info('價: %f', v2)
            logging.info('三日線: %d', cont_days)
            logging.info('高點: %.2f', get_higher_point)
        elif not cont_days > 0:
            logging.debug('%s三日線沒上漲: %d', lastStcok.date, cont_days)
        elif not self.__how_variety_volumn(index)[0] < 0:
            logging.debug('%s量沒縮: %d', lastStcok.date, self.__how_variety_volumn(index)[0])
        elif not self.__how_variety_close_price(index)[0] == 0:
            logging.debug('%s價沒平: %d', lastStcok.date, self.__how_variety_close_price(index)[0])
        return result

    def __get_higher_point(self, source, index):
        range = len(source[0: -index])

        sortd = sorted(source[0: -index])
        low_range, high_range = self.__get_higher_range(range)
        return sortd[low_range]

    def __get_higher_range(self,range):

        return int(range - math.floor(range / 3)), range

    def __how_variety_volumn(self, index):
        """
            量的變化
                Args:
                    index表示在目前總清單中的位置
                Returns: 
                    1上漲中; 0平穩; -1下跌中
        """
        ma, cont_days = self._grs_stock.MAV(MA_10)
        averageValue = (ma[-index]*1000 - self._stocks[-index].total_stocks)/self._stocks[-index].total_stocks
        if abs(averageValue) < ACCEPTABLE_PERCENTAGE :
            return 0, averageValue
        elif averageValue > 0:
            return -1, averageValue
        elif averageValue < 0:
            return 1, averageValue
        else:
            raise Exception('WTF! Apper impossible averageValue')

    def __how_variety_close_price(self, index):
        """價的變化
            return: 1上漲中; 0平穩; -1下跌中
        """
        ma, cont_days = self._grs_stock.MA(MA_10)
        averageValue = (ma[-index] - self._stocks[-index].close_price)/self._stocks[-index].close_price
        if abs(averageValue) < ACCEPTABLE_PERCENTAGE :
            return 0, averageValue
        elif averageValue > 0:
            return -1, averageValue
        elif averageValue < 0:
            return 1, averageValue
        else:
            raise Exception('WTF! Apper impossible averageValue')

    def cal_continue(self, list_data):
        """ 計算持續天數

            Rtype: int
            Returns: 向量數值：正數向上、負數向下。
        """
        diff_data = []
        for i in range(1, len(list_data)):
            if list_data[-i] > list_data[-i - 1]:
                diff_data.append(1)
            else:
                diff_data.append(-1)
        cont = 0
        for value in diff_data:
            if value == diff_data[0]:
                cont += 1
            else:
                break
        return cont * diff_data[0]

    def __init__(self, stockno, grs_stock):
        super(StockAnalysis, self).__init__()
        self._stocks = []
        self._grs_stock = grs_stock
        for raw in self._grs_stock.raw:
            self._stocks.append(YCStock(stockno, raw))

