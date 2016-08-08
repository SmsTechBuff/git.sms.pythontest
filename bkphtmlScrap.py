import urllib2
import re
from bs4 import BeautifulSoup
import datetime
import time
import csv
import urllib

#contenturl = "http://bmseek.tk/index.php?zip=40229&itemID=49767337"
#contenturl = "http://bmseek.tk/index.php?zip=40229&itemID=36483179"
#contenturl="http://bmseek.tk/index.php?zip=40229&itemID=37648910000"
# url1 = "http://bmseek.tk/index.php?zip=40229&itemID=37648910"
# url2 = "http://bmseek.tk/index.php?zip=40229&itemID=36483179"
# cUrl= []
# cUrl.append(url1)
# cUrl.append(url2)
# cUrl.append("http://bmseek.tk/index.php?zip=40229&itemID=49535121")

BMSEEKURL="http://bmseek.tk/index.php?zip=40229&itemID="

current_timestamp=datetime.datetime.fromtimestamp(time.time()).strftime('%m_%d_%Y_%H_%M_%S')
b = open('C:/WalmartStockResults/Wal_Scan_'+current_timestamp+'.csv', 'wb')

itemFile=open('C:/WalmartStockResults/ItemFile/itemfile_'+current_timestamp+'.txt', 'w')

logFile=open('C:/WalmartStockResults/log/loFile_'+current_timestamp+'.txt', 'w')

target_url="http://userquote.com/tools/record.txt"
response = urllib.urlopen(target_url)
data = response.readlines()

walmart_item_number=[]
for line in data:
    #print line
    itemFile.write(line)
    words =line.split(",")
    if len(words)>2 :
        if words[0]== "WALMART":
            print words[0],"->",words[1]
            print >>logFile,words[0],"->",words[1]  
            walmart_item_number.append(words[1].strip())  
        

itemFile.close()

print str(len(walmart_item_number))
print >>logFile,str(len(walmart_item_number))



itemlist=list(set(walmart_item_number))

print len(itemlist)
print >>logFile,str(len(walmart_item_number))

for item in walmart_item_number:
    print item



cUrl=[BMSEEKURL+s.strip() for s in itemlist]

print cUrl
print >>logFile, cUrl

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

headerDataset.append(header)
a = csv.writer(b)
a.writerows(headerDataset)


for contenturl in cUrl:
    
    print "Scan start.................."
    
    print >>logFile, "Scan...start...."
    
    soup = BeautifulSoup(urllib2.urlopen(contenturl).read())
    n=100
    newColumn = [[] for index in range(1, n)]
    product_info = soup.findAll("div", { "class" : "productInfo" })
    s = re.split(r'(<b>|<br/>| : )',str(product_info))
    
    product_name=s[4]
    item_code=s[8]
    walmart_price=s[16]
    
    print "prod: ", product_name," ",item_code," ",walmart_price
    
    print >>logFile, "prod: ", product_name," ",item_code," ",walmart_price
    
    
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
    a.writerows(data)
    print "SCAN END---FOR....","item code: ",item_code,"prod: ", product_name
    print >>logFile,"SCAN END---FOR....","item code: ",item_code,"prod: ", product_name
b.close()

print '##########################################'
print '##########################################'
print 'PROGRAM END!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
print '##########################################'
print '##########################################'


print >>logFile,'##########################################'
print >>logFile,'##########################################'
print >>logFile,'PROGRAM END!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
print >>logFile,'##########################################'
print >>logFile,'##########################################'

