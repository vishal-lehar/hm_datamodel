#!/usr/bin/python
import pandas as pd                #for handling datasets
#import statsmodels.api as sm       #for statistical modeling
import pylab as pl                 #for plotting
import numpy as np                 #for numerical computation
from functools import reduce

dfFinal = pd.read_csv("/home/dccom/vpaliwal/hm/hmFinal.csv")

#print(dfFinal.head())
#print(dfFinal.describe())  
#print(dfFinal.std()) 
#print(dfFinal.sort_values(['amount', 'race']))
#print(dfFinal.sort_values(['amount', 'race']))
print("##### Amount Analysis######")
print(dfFinal['amount'].describe())  
print("##### Weight Analysis ######")
print(dfFinal['weight'].describe())  
print(dfFinal['weight'].cov(dfFinal['amount']))  
print("##### Race Analysis ######")
print(dfFinal['race'].describe())  
print("##### Groupby Amount Analysis ######")
print(dfFinal.groupby('amount').mean())  
#print(dfFinal['height'].describe())  
#print(dfFinal['lab_result_1'].describe())  
#print(dfFinal['lab_result_2'].describe())  
#print(dfFinal['lab_result_3'].describe())  
#print(dfFinal['amount'].sum())  
#print(dfFinal['race'].describe())  
#print(dfFinal['gender'].describe())  
#print(dfFinal.mean(axis=0))

#print('Total amount spent:', dfFinal['amount'].sum())
#print('Min amount spent:', dfFinal['amount'].min())
#print(dfFinal[(dfFinal['weight'] > 70) & (dfFinal['amount'] > 7000)])

"""
pd.crosstab(dfFinal.gender, dfFinal.gender.astype(object)).plot(kind='bar')
pl.title('Amount paid by pateints')
pl.xlabel('Amount')
pl.ylabel('Gender')
pl.show()
"""
