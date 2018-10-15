#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:L
# Date:2018/8/28 15:03
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
# print(iris.data)
clf = tree.DecisionTreeClassifier(max_depth=2)
clf.fit(iris.data,iris.target)
print(clf.predict(iris.data))
tree.export_graphviz(clf,out_file='tree.dot')
from IPython.display import Image

print(Image('tree.png'))
