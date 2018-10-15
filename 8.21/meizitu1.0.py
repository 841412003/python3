#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:L
# Date:2018/8/24 17:01
import requests
from bs4 import BeautifulSoup

def get_page_number(num):
    url = 'http://www.mmjpg.com/home/' + num
    # 构造每个分页的网址
    response = requests.get(url).content
    