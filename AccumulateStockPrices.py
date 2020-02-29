# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 18:01:56 2020

@author: nifaullah
"""


import StockPriceByMinute as sm


_path = "C:/Users/nifaullah/Downloads/msba/WinBreak/DLA/StockData"
_filepath = f"{_path}/StockData.xlsx"
_companies = ["MSFT", "AAPL", "GOOG", "FB", "TWTR"]

df = sm.Build(_companies)