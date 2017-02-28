# -*- coding: utf-8 -*-
import logging
import logging.config
from stockAnalysis import StockAnalysis
from grs import Stock, RealtimeWeight

logging.config.fileConfig('../logging.conf', disable_existing_loggers=True)
logger = logging.getLogger(__name__)

def main():
    """
        mas count = 讀取的資料的月數的總開盤天數 - (5 - 1) 5 = MA day
        http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/STOCK_DAY_print.php?genpage=genpage/' +
            'Report%(year)d%(mon)02d/%(year)d%(mon)02d_F3_1_8_%(stock)s.php' +
            '&type=csv&r=%(rand)s'

        大盤資訊
        POST application/x-www-form-urlencoded
        http://www.twse.com.tw/ch/trading/exchange/FMTQIK/FMTQIK.php
        query_year=2017
        query_month=2
        download=csv
    """    
    logger.debug('start...')
    for stockno in ['2340']:
        # '2618', '3645', '2340', '4938'
        logging.debug("正在分析的股票是%s", stockno)
        stock = Stock(stockno, 12)                         # 預設是3個月    
        analysis_machine = StockAnalysis(stockno, stock)
        analysis_machine.analysis()

    # realtime_weight = RealtimeWeight()  # 擷取即時大盤資訊
    # print realtime_weight.raw                 # 原始檔案
    # stock.out_putfile('/dev/2618.csv')

    logger.debug('end...')

if __name__ == '__main__':
    main()
