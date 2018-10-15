#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:L
# Date:2018/8/29 15:42
from  itertools import product
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
X = iris.data[:,[2,3]]
y = iris.target
clf = tree.DecisionTreeClassifier(max_depth=2)
clf.fit(X,y)
plt.scatter(X[:,0],X[:,1],color='black')
# plt.show()
x_min,x_max = X[:,0].min()-1,X[:,0].max()+1
y_min,y_max = X[:,1].min()-1,X[:,1].max()+1
xx,yy = np.meshgrid(np.arange(x_min,x_max,0.1),
                    np.arange(y_min,y_max,0.1))
plt.plot()
Z = clf.predict(np.c_[xx.ravel(),yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contour(xx,yy,Z,alpha = 0.4,cmap = plt.cm.rainbow)
plt.scatter(X[:,0],X[:,1],c=y,alpha=1,cmap=plt.cm.rainbow)
plt.title('Decision Tree')
plt.xlabel('Lengeth')
plt.ylabel('width')
plt.show()