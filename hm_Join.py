#!/usr/bin/python
import pandas as pd                #for handling datasets
import numpy as np                 #for numerical computation
from functools import reduce

dfBill_amount = pd.read_csv("/home/dccom/vpaliwal/hm/bill_amount.csv")
dfBill_id = pd.read_csv("/home/dccom/vpaliwal/hm/bill_id.csv")
dfCl_data = pd.read_csv("/home/dccom/vpaliwal/hm/clinical_data.csv")
dfDemo = pd.read_csv("/home/dccom/vpaliwal/hm/demographics.csv")

dfB = [dfBill_amount, dfBill_id]

dfBill = reduce(lambda left,right: pd.merge(left,right,on='bill_id'), dfB)

#print(dfCl_data.head())
dfCl_data.rename(columns={'id': 'patient_id'}, inplace=True)

dfF = [dfBill, dfCl_data, dfDemo]

dfFinal = reduce(lambda left,right: pd.merge(left,right,on='patient_id'), dfF)
dfFinal.to_csv("/home/dccom/vpaliwal/hm/hmFinal.csv", sep=',', encoding='utf-8', index=False)

#print(dfFinal.head())
#print(dfFinal.describe())
#print(dfFinal.std())
#print(dfFinal.sort_values(['amount', 'race']))
#print(dfFinal.sort_values(['amount', 'race']))
#print(dfFinal['amount'].describe())
#print(dfFinal['amount'].sum())
#print(dfFinal['race'].describe())
#print(dfFinal['gender'].describe())
#print(dfFinal.mean(axis=0))
#print('Total amount spent:', dfFinal['amount'].sum())
#print('Min amount spent:', dfFinal['amount'].min())
#print(dfFinal[(dfFinal['weight'] > 70) & (dfFinal['amount'] > 7000)])
