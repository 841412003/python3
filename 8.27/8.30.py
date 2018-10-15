#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:L
# Date:2018/8/30 20:01
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn import tree
iris = load_iris()
X = iris.data[:,[2,3]]
y = iris.target
clf = LogisticRegression()
clf.fit(X,y)
x_min,x_max = X[:,0].min()-1,X[:,0].max()+1
y_min,y_max = X[:,1].min()-1,X[:,1].max()+1
xx,yy = np.meshgrid(np.arange(x_min,x_max,0.1),
                    np.arange(y_min,y_max,0.1))
Z = clf.predict(np.c_[xx.ravel(),yy.ravel()])
Z = Z.reshape(xx.shape)
plt.plot()
plt.contour(xx,yy,Z,alpha = 0.4,cmap = plt.cm.rainbow)
plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.brg)
plt.title('Decision Tree')
plt.xlabel('Lengeth')
plt.ylabel('width')
plt.show()