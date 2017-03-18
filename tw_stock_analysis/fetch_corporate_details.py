# -*- coding: utf-8 -*-
import csv
import logging
import urllib3
from cStringIO import StringIO
from urllib import urlencode

TWSE_HOST = 'http://www.twse.com.tw/'
TWSE_CONNECTIONS = urllib3.connection_from_url(TWSE_HOST)

class FetchCorporateDetails(object):
    """抓取三大法人的買賣超明細"""
    def fetch_data(self, date):
        encoded_body = {
            "download": "csv",
            "qdate": date,
            "sorting": "by_issue",
            "select2": "ALLBUT0999",
        }

        http = urllib3.PoolManager()
        body, content_type = (urlencode(encoded_body or {}),
                                    'application/x-www-form-urlencoded')
        headers = {}
        headers.update({'Content-Type': content_type, 'Accept-Encoding': 'gzip, deflate'})
        

        r = TWSE_CONNECTIONS.urlopen('POST', '/ch/trading/fund/T86/T86.php',
                 headers=headers,
                 body=body)
       
        print r.Content-Type
        # with open('../logs/test.csv', 'wb') as out:
        #     while True:
        #         data = r.read(2)
        #         if not data:
        #             break
        #         out.write(data)

        r.release_conn()
        
        # print self.to_list(csv_files)

    def to_list(self, csv_file):
        """ 串接每日資料 舊→新

            :param csv csv_file: csv files
            :rtype: list
        """
        tolist = []
        for i in csv_file:
            print i 
            i = [value.strip().replace(',', '') for value in i]
            try:
                for value in (1, 2, 3, 4, 5, 6, 8):
                    i[value] = float(i[value])
            except (IndexError, ValueError):
                pass
            tolist.append(i)
       
        if tolist:
            self.__info = (tolist[0][0].split(' ')[1],
                           tolist[0][0].split(' ')[2].decode('cp950'))
            self.__raw_rows_name = tolist[1]
            return tuple(tolist[2:])
        return tuple([])
       
    def __init__(self):
        super(FetchCorporateDetails, self).__init__()


if __name__ == '__main__':
    service = FetchCorporateDetails()
    service.fetch_data('106/02/24')

        