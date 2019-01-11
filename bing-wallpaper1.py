# -*- coding: utf-8 -*-
import schedule
import time
import sys
import os
import random
import glob             # ->added to make pics upload -> see job8
import threading        # ->added to make multithreadening possible -> see fn run_threaded
import requests
import json
import urllib.request
from random import randint
import time


def job1():
    url = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx='+str(randint(1, 7))+'&n=1&nc=1547229581406&pid=hp&toWww=1&redig=8309AB5D45A046129EF14320392375BE'
    response = requests.get(url)
    jsonres = json.loads(response.text)
    print('https://www.bing.com'+jsonres['images'][0]['url'])
    imgLink = 'https://www.bing.com'+jsonres['images'][0]['url']
    imgName = (imgLink.split('/'))
    countspl = len(imgName)
    countspl = countspl - 1
    print(imgName[countspl])
    urllib.request.urlretrieve(imgLink, imgName[countspl])



# function to make threads -> details here http://bit.ly/faq_schedule
def run_threaded(job_fn):
    job_thread = threading.Thread(target=job_fn)
    job_thread.start()

#schedule.every(1).hour.do(run_threaded, job1)              # get stats
schedule.every(1).second.do(run_threaded, job1)              # get img

while True:
    schedule.run_pending()
    time.sleep(1)