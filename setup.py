#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twss_analysis
from setuptools import setup, find_packages

long_description = open('./README.md', 'r').read()
description = '台灣上市股票價格擷取（Fetch Taiwan Stock Exchange data）'

setup(name='twss_analysis',
      version='1.0.1',
      description=description,
      long_description=long_description,
      author='YUCHEN LIU',
      author_email='steny138@gmail.com',
      url='https://github.com/steny138/PythonTwssAnalysis',
      packages=['twss_analysis'],
      package_data={'twss_analysis': ['*.csv']},
      include_package_data=True,
      license='LICENSE',
      keywords="Taiwan Stock Exchange twse twss " + \
               "台灣 台北 股市 即時 上市 上櫃",
      install_requires=['python-dateutil==1.5', 'ujson', 'urllib3'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Financial and Insurance Industry',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: Chinese (Traditional)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Topic :: Office/Business :: Financial :: Investment',
          ],
     )
