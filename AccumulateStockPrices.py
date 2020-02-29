# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 18:01:56 2020

@author: nifaullah
"""


import StockPriceByMinute as sm


_path = "" # Provide local path
_filepath = f"{_path}/StockData.xlsx" # Change filename if you want
_companies = ["MSFT", "AAPL", "GOOG", "FB", "TWTR"] # Add or remove companies as per your requiremen

sm.Build(_companies, _filepath)
