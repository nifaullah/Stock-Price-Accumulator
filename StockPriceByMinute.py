# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 10:55:32 2020

@author: nifaullah
"""
import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import os



# =============================================================================
# Function to fix column Names : Gets Dataframe & returns dataframe after
#   fixing columns 
# =============================================================================
def FixColumnNames(df, label, single = False):
    df = df.copy()
    getLabel = lambda text1,text2,single: f"{text2}_{text1}" if single else f"{text1}_{text2}"
    for col in df.columns:
        df[getLabel(col, label, single)] = df[col]
        df.drop(col, axis = 1,inplace=True)
    return df


# =============================================================================
# Function: Build
# Inputs:
#   1. companies - List of companies or a single company as string
#   2. filepath - physical path where the file is stored or to be created along
#       with filename and extension. If not provided dataframe is not saved.
# Output: Pandas DataFrame containing minute level data of volumes & close of
#   the inputted companies
# =============================================================================
def Build(companies, filepath=""):
    # Return if no companies provided
    if not companies:
        return 'Please provide code of atleast one company'
    
    # Constants
    _index_label = "Datetime"
    _no_of_days = "1D"
    _date_format = "%Y-%m-%d"
    _interval = "1m"
    _close_label = "Close"
    _volume_label = "Volume"
    _max_days_allowed_per_call = 7
    _max_past_days_allowed = 29
    
    # Variable Definitions
    is_file_available = os.path.isfile(filepath)
    current_date = datetime.today().date() -  timedelta(days = 1)
    end_date = datetime.today().date()
    start_date = current_date - timedelta(days = _max_days_allowed_per_call - 1)
    diff = _max_past_days_allowed
    last_date = None
    results_df = pd.DataFrame()
    if len(companies) > 1 and type(companies) != str:
        close_label = close_addon_label = _close_label
        volume_label = volume_addon_label = _volume_label
        single = False
    else:
        close_label = [_close_label]
        volume_label = [_volume_label]
        if type(companies) != str:
            close_addon_label = volume_addon_label = companies[0].upper()
        else:
            close_addon_label = volume_addon_label = companies.upper()
        single = True
    
    if is_file_available:
        results_df = pd.read_excel(filepath)
        results_df.set_index(_index_label, inplace=True)
        last_date = results_df.last(_no_of_days).index[len(results_df.last(_no_of_days).index)-1].date()
        diff = (current_date - last_date).days
        if (last_date != current_date) & (diff <= _max_past_days_allowed):
            startDate = end_date
    
    # Loading Data from Yahoo Finance API
    # Looping as API allows only 7 days of data retrieval in one call
    # Further API allows upto 30 days of past data with 1 minute interval
    is_diff_positive = is_file_changed = (last_date != current_date)
    while is_diff_positive:
        df = yf.download(companies, start=start_date.strftime(_date_format), end = end_date.strftime(_date_format), interval = _interval)
        df = FixColumnNames(df[close_label], close_addon_label, single).join(FixColumnNames(df[volume_label], volume_addon_label, single))
        df.index = df.index.tz_localize(None)
        results_df = pd.concat([results_df,df])
        if diff < _max_days_allowed_per_call:
            is_diff_positive = False
        diff = diff - _max_days_allowed_per_call
        end_date = start_date
        days = min(abs(diff),_max_days_allowed_per_call)
        start_date = start_date - timedelta(days = days)
    
    
    # Excel does not allow timezone aware index, therefore changing it to Naive
    results_df.index = results_df.index.tz_localize(None)
    results_df = results_df.sort_index()
    
    # Save only if original file is changed & if a filepath is provided
    if is_file_changed and (filepath):
        results_df.to_excel(filepath)
        return
        
    return results_df