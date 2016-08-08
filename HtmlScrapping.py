

import urllib2
from bs4 import BeautifulSoup

contenturl = "http://bmseek.tk/index.php?zip=40229&itemID=45821220"
soup = BeautifulSoup(urllib2.urlopen(contenturl).read())

table = soup.find('table', id="example")
#table = soup.find('table')
#id="example" class="display"

for br in soup.find_all("br"):
    br.replace_with(",")
#print soup

rows = table.findAll('tr')
#print"rows:"
#print rows



print "new new new new new"

data = []
#table = soup.find('table', attrs={'class':'lineItemsTable'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [str(ele.text.strip()).replace("&nbsp"," ") for ele in cols]
    print cols

    data.append([ele for ele in cols if ele]) # Get rid of empty values

print data


import csv
b = open('C:/WalmartStockResults/test.csv', 'w')
a = csv.writer(b)
a.writerows(data)
b.close()