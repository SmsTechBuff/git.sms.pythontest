
from threading import Thread
import urllib2
import re
from bs4 import BeautifulSoup
import datetime
import time
import csv
import urllib
import Queue
import mechanize
from pip._vendor.distlib.locators import Page


# this program extracts the walmart itemlist from brickseek

url1 = "http://brickseek.com/clearance/deals/all/new/?p="
url2 = "&s=3,13"

url=[]
for i in range(1,30):
    url.append(url1+str(i)+url2)

WalmartItemList=[]

for contenturl in url:
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
     
    response = opener.open(contenturl)
    page = response.read()
    
    
    soup = BeautifulSoup(page)
    html=soup.prettify()
    
    x=[]
    for link in soup.findAll('a', href=re.compile('sku=')):
        x= re.split(r'=|',link['href'])
        WalmartItemList.append("WALMART,"+x[1]+",40229\n")

print len(WalmartItemList)

current_timestamp=datetime.datetime.fromtimestamp(time.time()).strftime('%m_%d_%Y_%H_%M_%S')
itemFile=open('C:/WalmartStockResults/ItemFile/itemfile_'+current_timestamp+'.txt', 'w')

for walItem in WalmartItemList:
    itemFile.write(walItem)
itemFile.close()


