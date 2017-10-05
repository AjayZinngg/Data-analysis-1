# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:27:37 2017

@author: zinngg
"""

import pandas as pd

df1 = pd.read_csv("data.csv")
#1.
print(df1.loc[:,[ "customer_id" ,"Transactions"]]) #
#2.
df1.rename(columns={'customer_id':'user_id'}, inplace=True)
print(df1)

#3.
print(df1.loc[df1['category_id'] == 'FNB', 'GR' ].mean())

#4.
print(df1.loc[(df1['category_id'] == 'GTW')&(df1['TransactionValue'] > 0),'user_id' ])

#5.
print(df1.groupby('category_id')['Transactions'].sum().idxmax())
#6.
#df1['date'] = pd.to_datetime(df1['date'])
#print(df1.groupby(pd.Grouper(key = 'date', freq='M')))

