# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('..')

from grs import Stock
from tw_stock_analysis.stockAnalysis import StockAnalysis

class StockAnalysisTestCase(unittest.TestCase):
    """測試藏股分析"""
    def setUp(self):
        stockno = '2618'
        stock = Stock(stockno, 1)
        self.stockAnalysis = StockAnalysis(stockno, stock)
 
    def tearDown(self):
        pass

    def test_calculate_continue_days(self):
        """
            測試計算計算天數
        """
        # Arrange
        list_data = [1,2,3,4,5,0,-1,-2,-3]
        expectedDays = -4

        # Act
        actualDays = self.stockAnalysis.cal_continue(list_data)

        # Assert
        self.assertEquals(expectedDays, actualDays);
        pass

    def test_notHigh_averageUp_valueDown_priceSame(self):
        index = 1

        actual = self.stockAnalysis.is_notHigh_averageUp_valueDown_priceSame(index)

        self.assertFalse(actual)

    def test_moreLow_averageDown_valueUp_priceDown(self):
        """
            歷史行情看股價偏低
                + 量增 ＆ 價跌 代表 上漲的開始
        """
        index = 1 

        actual = self.stockAnalysis.is_moreLow_averageDown_valueUp_priceDown(index)

        self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()