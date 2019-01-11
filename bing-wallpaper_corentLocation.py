#!/usr/bin/env python
# -*- coding: utf-8 -*-

import schedule
import requests
import os
import os.path
from pathlib import Path
import json
import urllib.request
from random import randint
import time


def job():
    url = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx='+str(randint(1, 7))+'&n=1&nc=1547229581406&pid=hp&toWww=1&redig=8309AB5D45A046129EF14320392375BE'
    response = requests.get(url)
    jsonres = json.loads(response.text)
    print('https://www.bing.com'+jsonres['images'][0]['url'])
    imgLink = 'https://www.bing.com'+jsonres['images'][0]['url']
    imgName = (imgLink.split('/'))
    countspl = len(imgName)
    countspl = countspl - 1
    print(imgName[countspl])
    fileimg = Path(os.getcwd()+'/'+imgName[countspl])
    if fileimg.is_file():
        os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri " + os.getcwd() + '/' + imgName[countspl])
    else:
        urllib.request.urlretrieve(imgLink, imgName[countspl])
        print(os.getcwd()+'/'+imgName[countspl])
        os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri "+os.getcwd()+'/'+imgName[countspl])
        #/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/mohammad/Pictures/Wallpapers/709477.png

def job2():
    print("I'm working...")

#schedule.every(1).second.do(job)
schedule.every(30).minutes.do(job)
#schedule.every(10).minutes.do(job2)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
