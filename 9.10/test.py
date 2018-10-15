#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:L
# Date:2018/9/19 18:13
from goose3 import Goose
from goose3.text import StopWordsChinese


def gooseExample():
    g = Goose({'stopwords_class': StopWordsChinese})
    url = "https://item.btime.com/36a0f17i0489keqltn35q96p4lr?from=haozcxw"
    article = g.extract(url=url)
    print(article.title)
    print(article.cleaned_text)


def gooseChineseExample():
    g = Goose({'stopwords_class': StopWordsChinese})
    url = "https://item.btime.com/36a0f17i0489keqltn35q96p4lr?from=haozcxw"
    article = g.extract(url=url)
    print(article.title)
    print(article.meta_description)
    print(article.cleaned_text[:150])


if __name__ == '__main__':
    # begin_insert_job("knowledge", "person", "../data/Person.json")
    gooseExample()
    gooseChineseExample()
