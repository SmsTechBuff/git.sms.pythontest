from threading import Thread
import urllib2
import re
from bs4 import BeautifulSoup
import datetime
import time
import csv
import urllib
import Queue
import os



#####################################################
# HTML SCRAPPING WITH MULTI THREADED APPROACH
#####################################################

def htmlScrap(contenturl):
#    for contenturl in cUrl:
    
    print "Scan start.................."
    
    #print >>logFile, "Scan...start...."
    
    soup = BeautifulSoup(urllib2.urlopen(contenturl).read())
    n=100
    newColumn = [[] for index in range(1, n)]
    product_info = soup.findAll("div", { "class" : "productInfo" })
    s = re.split(r'(<b>|<br/>| : )',str(product_info))
    
    product_name=s[4]
    item_code=s[8]
    walmart_price=s[16]
    
    print "prod: ", product_name," ",item_code," ",walmart_price
    
    #   print >>logFile, "prod: ", product_name," ",item_code," ",walmart_price
    
    
    table = soup.find('table', id="example")
    
    for br in soup.find_all("br"):
        br.replace_with(",")
    
    rows = table.findAll('tr')
    
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    
    for row in rows:
        cols = row.find_all('td')
        i=0
        newColumn[i].append(product_name[0:30])
        i+=1
        newColumn[i].append(item_code)
        i+=1
        newColumn[i].append(walmart_price)
        i+=1
    
        for c in cols:
            #print "value of c = ", c
            column = re.split(r',|<td>|</td>|<b>|</b>|<br/>|<a|</a>| : |&amp;nbsp|<|>',str(c).replace("<td></td",", ,"))
            #print column
            #newColumn[i].append([])
            if column:
                for c1 in column:
                    if  c1 and not("\"" in c1) and not (" Google maps" in c1):
                        #print "current i",i," val c= ",c1
                        newColumn[i].append(c1)
                        #print newColumn
                        i=i+1
                
        
        newColumn[i].append(product_name)
        i+=1
        
    data=map(list,map(None,*newColumn))
    
    #a.writerows(data)
    print "SCAN END---FOR....","item code: ",item_code,"prod: ", product_name," # of Store : ", str(len(data))
    #    print >>logFile,"SCAN END---FOR....","item code: ",item_code,"prod: ", product_name
    return data



def str_to_int(arg, queue):
    result=[]
    result = htmlScrap(arg)
    queue.put(result)

def combine():
    #arguments = ('49767337','44931471','47348001','46429971')
    BMSEEKURL="http://bmseek.tk/index.php?zip=40229&itemID="
    
    
    # read the latest item file created by the createWalItemList.py in the Itelfile directory
    itemdir='C:/WalmartStockResults/ItemFile/' # path to your log directory
    itemfiles = sorted([ f for f in os.listdir(itemdir) if f.startswith('itemfile_')])
    print "Most recent file = %s" % (itemdir+itemfiles[-1],)
    itemFileName=itemdir+itemfiles[-1]
    with open(itemFileName) as f:
        data=f.readlines()
    
    
    walmart_item_number=[]
    for line in data:
        #print line
        #itemFile.write(line)
        words =line.split(",")
        if len(words)>2 :
            if words[0]== "WALMART":
                print words[0],"->",words[1]
                #print >>logFile,words[0],"->",words[1]  
                walmart_item_number.append(words[1].strip())  
            
    
    #itemFile.close()
    
    print str(len(walmart_item_number))
    itemlist=list(set(walmart_item_number))
    
    q = Queue.Queue()
    threads = []

#since there are over 1500 item hence create less than 100 threads per iteration

#Split the list into smaller chunks of 100

    chunks=[]
    chunksize=250
    chunks = [itemlist[x:x+chunksize] for x in xrange(0, len(itemlist), chunksize)]


    for chunk in chunks:
        for argument in chunk:
            print "smaller chunk lenght: ", len(chunk)
            t = Thread(target=str_to_int, args=(BMSEEKURL+argument, q))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

    return [q.get() for _ in xrange(len(itemlist))]


current_timestamp=datetime.datetime.fromtimestamp(time.time()).strftime('%m_%d_%Y_%H_%M_%S')
b = open('C:/WalmartStockResults/Wal_Scan_'+current_timestamp+'.csv', 'wb')

headerDataset=[]

header=[]
header.append("ItemName")
header.append("Item Number#")
header.append("Online Price#")
header.append("Walmart#")
header.append("Walmart Name")
header.append("Street")
header.append("City")
header.append("State")
header.append("Zip")
header.append("Phone")
header.append("Distance")
header.append("Quantity")
header.append("Status")
header.append("Store Price")
header.append("Aisle Number")
header.append("Price Diff")
header.append("Full Item Desc")



a = csv.writer(b)
headerDataset.append(header)
a.writerows(headerDataset)


for ele in combine():
        print ele
        a.writerows(ele)
    

