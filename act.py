#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
import json
import urllib.request
from random import randint
import time

def DownImg(num):
    url = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx='+str(num)+'&n=1&nc=1547229581406&pid=hp&toWww=1&redig=8309AB5D45A046129EF14320392375BE'
    response = requests.get(url)
    jsonres = json.loads(response.text)
    print('https://www.bing.com'+jsonres['images'][0]['url'])
    imgLink = 'https://www.bing.com'+jsonres['images'][0]['url']
    imgName = (imgLink.split('/'))
    countspl = len(imgName)
    countspl = countspl - 1
    print(imgName[countspl])
    urllib.request.urlretrieve(imgLink, imgName[countspl])

count = 0
while(count <=6):
    DownImg(randint(1, 7))
    time.sleep(60)
    count += 1

'''
url = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=2&n=1&nc=1547229581406&pid=hp&toWww=1&redig=8309AB5D45A046129EF14320392375BE'
response = requests.get(url)
jsonres = json.loads(response.text)
print('https://www.bing.com'+jsonres['images'][0]['url'])

url = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=3&n=1&nc=1547229581406&pid=hp&toWww=1&redig=8309AB5D45A046129EF14320392375BE'
response = requests.get(url)
jsonres = json.loads(response.text)
print('https://www.bing.com'+jsonres['images'][0]['url'])

url = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=4&n=1&nc=1547229581406&pid=hp&toWww=1&redig=8309AB5D45A046129EF14320392375BE'
response = requests.get(url)
jsonres = json.loads(response.text)
print('https://www.bing.com'+jsonres['images'][0]['url'])

url = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=5&n=1&nc=1547229581406&pid=hp&toWww=1&redig=8309AB5D45A046129EF14320392375BE'
response = requests.get(url)
jsonres = json.loads(response.text)
print('https://www.bing.com'+jsonres['images'][0]['url'])

url = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=6&n=1&nc=1547229581406&pid=hp&toWww=1&redig=8309AB5D45A046129EF14320392375BE'
response = requests.get(url)
jsonres = json.loads(response.text)
print('https://www.bing.com'+jsonres['images'][0]['url'])

url = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=7&n=1&nc=1547229581406&pid=hp&toWww=1&redig=8309AB5D45A046129EF14320392375BE'
response = requests.get(url)
jsonres = json.loads(response.text)
print('https://www.bing.com'+jsonres['images'][0]['url'])
'''