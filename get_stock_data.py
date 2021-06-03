#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 20:34:21 2021

@author: ashwinruthesh
"""
# Importing the modules necessary

import pandas as pd
import yfinance as yf
import pickle 
import os


# nifty = pd.read_csv('nifty_next50.csv', index_col=0)
# tickers = nifty['Symbol']

# os.makedirs('nfty_dfs')

def get_stock_data():
    nifty = pd.read_csv('nifty_next50.csv', index_col=0)        # Reading in the csv file of NIfty Next 50 components      
    tickers = nifty['Symbol']                                   # and assigning the symbols to a seperate series 

    os.makedirs('nfty_dfs')  # Making a new directory to store the historical data the script will download 
    
    
    for ticker in tickers:
        if not os.path.exists('nfty_dfs/{}.csv'.format(ticker)):
            df = yf.download('{}.NS'.format(ticker), start='2000-01-01', end='2020-12-31')  # Downloading from yahoo finance and saving it to a CSV file.
            df.to_csv('nfty_dfs/{}.csv'.format(ticker)                                      # '.NS' is the code Yahoo finance appends to symbols of NSE listed companies
        else:
            print('Already have {}'.format(ticker))


# Now to compile all Adjusted Close values from the 50 companies to one single file.
# I will be using Adj Close values for all analysis 

def compile_adjcloses():
    nifty = pd.read_csv('nifty_next50.csv', index_col=0)
    tickers = nifty['Symbol']
    
    main_df = pd.DataFrame  # Creating an empty data frame into which Adj Close values will be iterated
    
    for ticker in tickers:
        df = pd.read_csv('nfty_dfs/{}.csv'.format(ticker))
        df.set_index('Date', inplace=True)
        
        df.rename(columns = {'Adj Close' : ticker}, inplace=True) # Renaming the adj close column to that of the company itself 
        df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace=True) # and dropping all other columns so Adj Close is the only price data that remains
        
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')  # Merging each adj close data to the empty dataframe as we iterate through them
    
    print(main_df.tail())
    main_df.to_csv('nfty_nxt50_closes.csv')  # Saving the merged adj closes as a csv file


#compile_adjcloses()

    
          





        
    
    
