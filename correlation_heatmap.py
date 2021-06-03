#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 18:12:58 2021

@author: ashwinruthesh
"""

import pandas as pd
import seaborn as sns 





# Reading in the csv file containing daily Adjusted closes

df = pd.read_csv('nfty_nxt50_closes.csv')
df.set_index('Date', inplace=True)

# Calculating the correlation of daily returns 

returns = df.pct_change()
corr_frame = returns.corr()

# Plotting onto a heatmap for easy visualization

ax = sns.heatmap(corr_frame, cmap='YlGnBu')
