#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:L
# Date:2018/8/30 20:15
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
def plot_estimator(estimator,X,y,title):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))
    Z = estimator.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.plot()
    plt.contour(xx, yy, Z, alpha=0.4, cmap=plt.cm.RdYlBu)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.brg)
    plt.title(title)
    plt.xlabel('Sepal.Length')
    plt.ylabel('Sepal.Width')
    plt.show()
iris = load_iris()
X = iris.data[:,[0,1]]
y = iris.target
clf = RandomForestClassifier(n_estimators=100,criterion="entropy",random_state=0)
clf.fit(X,y)
plot_estimator(clf,X,y,'RandomForestClassifier')
clf1 = SVC(kernel='rbf')
clf1.fit(X,y)
clf2 = DecisionTreeClassifier()
clf2.fit(X,y)
clf3 = RandomForestClassifier(n_estimators=10,criterion='entropy')
clf3.fit(X,y)
clf4 = LogisticRegression()
clf4.fit(X,y)
plot_estimator(clf1,X,y,'rbf')
plot_estimator(clf2,X,y,'DecisionTreeClassifier')
plot_estimator(clf3,X,y,'RandomForestClassifier')
plot_estimator(clf3,X,y,'LogisticRegression')
