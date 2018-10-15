#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:L
# Date:2018/8/30 23:10
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
import numpy as np
digits = load_digits()
fig = plt.figure(figsize=(8,8))
fig.subplots_adjust(left=0,right=1,bottom=0,top=1,hspace=0.05,wspace=0.05)
for i in range(36):
    ax = fig.add_subplot(6,6,i+1,xticks=[],yticks=[])
    ax.imshow(digits.images[i],cmap=plt.cm.binary,interpolation='nearest')
    ax.text(0,7,str(digits.target[i]),color = 'red',fontsize=20)
scaler = StandardScaler()
scaler.fit(digits.data)
X_scaled = scaler.transform(digits.data)
mlp = MLPClassifier(hidden_layer_sizes=(30,30,30),activation = 'logistic',max_iter=200)
mlp.fit(X_scaled,digits.target)
predicted = mlp.predict(X_scaled)
fig = plt.figure(figsize=(8,8))
fig.subplots_adjust(left=0,right=1,bottom=0,top=1,hspace=0.05,wspace=0.05)
for i in range(36):
    ax = fig.add_subplot(6,6,i+1,xticks=[],yticks=[])
    ax.imshow(digits.images[i],cmap=plt.cm.binary,interpolation='nearest')
    ax.text(0,7,str('{}-{}'.format(digits.target[i],predicted[i])),color = 'red',fontsize=20)
res=[]
for i,j in zip(digits.target,predicted):
    res.append(i==j)
print(sum(res)/len(digits.target))
plt.show()
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data[:,[0,1]]
y = iris.target