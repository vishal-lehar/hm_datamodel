#!/usr/bin/python
import pandas as pd                #for handling datasets
#import statsmodels.api as sm       #for statistical modeling
import pylab as plt                 #for plotting
import numpy as np                 #for numerical computation
from functools import reduce
import matplotlib.pyplot as plt

dfFinal = pd.read_csv("/home/dccom/vpaliwal/hm/hmFinal.csv")

#print(dfFinal.head())
#print(dfFinal.describe())  
#print(dfFinal.std()) 
#print(dfFinal.sort_values(['amount', 'race']))
#print(dfFinal.sort_values(['amount', 'race']))
print("##### Amount Analysis######")
print(dfFinal['amount'].describe())  
print("##### Top 10 Amounts ######")
#ten = dfFinal['amount'].value_counts()
print(dfFinal['amount'].value_counts())
print("##### Weight and Height Analysis ######")
print(dfFinal['weight'].describe())  
print(dfFinal['weight'].cov(dfFinal['amount']))  
print(dfFinal['height'].describe())  
print("##### Race Analysis ######")
print(dfFinal['race'].describe())  
print("##### Groupby Amount Analysis ######")
#print(dfFinal.groupby('amount').mean())  
print("##### Amount Height weight ######")
print(dfFinal[['amount', 'height', 'weight']].head())
#print(dfFinal['lab_result_1'].describe())  
#print(dfFinal['lab_result_2'].describe())  
#print(dfFinal['lab_result_3'].describe())  
#print(dfFinal['amount'].sum())  
#print(dfFinal['race'].describe())  
#print(dfFinal['gender'].describe())  
#print(dfFinal.mean(axis=0))

#print('Total amount spent:', dfFinal['amount'].sum())
#print('Min amount spent:', dfFinal['amount'].min())
#print("##### weight > 100 and amount > 20K ######")
#print(dfFinal[(dfFinal['weight'] > 100) & (dfFinal['amount'] > 20000)].describe())
'''
plt.figure()
dfFinal['weight'].iloc[5].plot(kind='bar')
cht = dfFinal['amount', 'weight'].pct_change()
plt.scatter(cht.weight, cht.amount)
plt.xlabel('weight')
plt.ylabel('amount')
plt.savefig('/home/dccom/vpaliwal/hm/hm_final.jpg')
'''
