#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:L
# Date:2018/9/10 10:24
import pandas
df = pandas.read_csv('customer_churn.csv',header=0,index_col=0)
df = df.ix[:,3:]
cat_var=['international_plan','voice_mail_plan','churn']
for var in cat_var:
    df[var] = df[var].map(lambda e:1 if e=='yes' else 0)
y = df.ix[:,-1]
x = df.ix[:,:-1]
print(df.columns)
