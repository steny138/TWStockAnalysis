# -*- coding: utf-8 -*-

class YCStock(object):
	"""docstring for YCStock"""
	"""
            0. 日期
            1. 成交股數
            2. 成交金額
            3. 開盤價
            4. 最高價（續）
            5. 最低價
            6. 收盤價
            7. 漲跌價差
            8. 成交筆數
    """
	def __init__(self, stockno, rawdata):
		super(YCStock, self).__init__()
		self.stockno = stockno
		self.date = rawdata[0]
		self.total_stocks = int(rawdata[1])
		self.total_amount = int(rawdata[2])
		self.open_price = float(rawdata[3])
		self.high_price = float(rawdata[4])
		self.low_price = float(rawdata[5])
		self.close_price = float(rawdata[6])
		self.diff_price = rawdata[7]
		self.deal_count = int(rawdata[8])