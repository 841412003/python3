# -*- coding: utf-8 -*-
from pytagcloud import create_tag_image, make_tags
newarr={}
with open('sqlshuju.txt','r',encoding='GBK') as f:
    arr=f.read().strip().split()
for k in arr:
    if k not in newarr:
        newarr[k]=1
    else:
        newarr[k]+=1
print(newarr)
from operator import itemgetter
swd = sorted(newarr.items(), key=itemgetter(1), reverse=True)
print(swd)
tags = make_tags(swd,maxsize = 120,minsize=50)
create_tag_image(tags, 'loud6.png',size=(540, 360),fontname="simhei")