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

    def test_is_nothigh_averageup_valuedown_pricesame(self):
        index = 1

        actual = self.stockAnalysis.is_nothigh_averageup_valuedown_pricesame(index)

        self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()