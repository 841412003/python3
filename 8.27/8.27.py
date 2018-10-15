#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:L
# Date:2018/8/27 17:00
import pandas
df = pandas.read_csv("house-prices.csv")
house = pandas.concat([df,pandas.get_dummies(df['Brick']),pandas.get_dummies(df['Neighborhood'])],axis=1)
del house['No']
del house['West']
del house['Brick']
del house['Neighborhood']
del house['Home']
X = house[['SqFt','Bedrooms','Bathrooms','Offers','Yes','East','North']]
Y = house['Price'].values
from sklearn.linear_model import LinearRegression
regr = LinearRegression()
regr.fit(X,Y)
import statsmodels.api as sm
X2 = sm.add_constant(X)
est = sm.OLS(Y,X2)
est2 = est.fit()
predictorcols = ['SqFt','Bedrooms','Bathrooms','Offers','Yes','East','North']
import itertools
AICs = {}
for k in range(1, len(predictorcols)+1):
    for variables in itertools.combinations(predictorcols, k):
        predictors = X[list(variables)]
        predictors2 = sm.add_constant(predictors)
        est = sm.OLS(Y, predictors2)
        res = est.fit()
        AICs[variables] = res.aic
from collections import Counter
c = Counter(AICs)
print(c.most_common()[::-10])
