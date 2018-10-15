#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:L
# Date:2018/9/26 8:44
import requests
from bs4 import BeautifulSoup
res = requests.get('https://new.qq.com/omn/20180929/20180929A0DX7Q.html')
soup = BeautifulSoup(res.text, 'html.parser')
newsary = []
for news in soup.select('.one-p'):
    # newsary.append(news.select('.one-p'[0].text))
    newsary.append(news.text)

print(newsary)
