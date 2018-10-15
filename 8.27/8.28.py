#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:L
# Date:2018/8/27 23:10
import pandas
df = pandas.read_excel('house_price_regression.xlsx')
df['age'] = df['age'].map(lambda e:2018-int(e.strip().strip('建筑年代：')))
df[['room','living_room']] = df['layout'].str.extract('(\d+)室(\d+)厅')
df['room'] = df['room'].astype(int)
df['living_room'] = df['living_room'].astype(int)
df['total_floor'] = df['floor_info'].str.extract('共(\d+)层')
df['total_floor'] = df['total_floor'].astype(int)
df['floor'] = df['floor_info'].str.extract('^(.)层')
df['direction'] = df['direction'].map(lambda  e:e.strip())
del df['layout']
del df['floor_info']
del df['title']
del df['url']
df = pandas.concat([df,pandas.get_dummies(df['direction']),pandas.get_dummies(df['floor'])],axis=1)
del df['南北向']
del df['低']
del df['floor']
del df['direction']
from matplotlib import pyplot as plt
df[['price','area']].plot(kind='scatter',x = 'area',y = 'price',figsize = [10,5])
y = df['price']
x = df[['area']]
from sklearn.linear_model import LinearRegression
regr = LinearRegression()
regr.fit(x,y)
plt.scatter(x, y, color='blue')
plt.plot(x,regr.predict(x),linewidth = 3,color='red')
plt.xlabel('area')
plt.ylabel('price')
plt.show()
import statsmodels.api as sm
X2 = sm.add_constant(x)
est = sm.OLS(y,X2)
est2 = est.fit()
predictorcols = ['age','area','room','living_room','total_floor','东南向','东向','南向','西南向','西向','中','高']
import itertools
AICs = {}
for k in range(1,len(predictorcols)+1):
    for variables in itertools.combinations(predictorcols,k):
        predictors = x[list(variables)]
        predictors2 = sm.add_constant(predictors)
        est = sm.OLS(y,predictors2)
        res = est.fit()
        AICs[variables] = res.aic
from collections import Counter
c = Counter(AICs)
c.most_common()[::-10]
print(c.most_common()[::-10])