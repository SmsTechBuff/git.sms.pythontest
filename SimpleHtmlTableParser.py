import lxml.html as LH
#import requests
#import pandas as pd
def text(elt):
    return elt.text_content().replace(u'\xa0', u' ')

url = 'http://www.fdmbenzinpriser.dk/searchprices/5/'
r = requests.get(url)
root = LH.fromstring(r.content)

for table in root.xpath('//table[@id="sortabletable"]'):
    header = [text(th) for th in table.xpath('//th')]        # 1
    data = [[text(td) for td in tr.xpath('td')]  
            for tr in table.xpath('//tr')]                   # 2
    data = [row for row in data if len(row)==len(header)]    # 3 
    data = pd.DataFrame(data, columns=header)                # 4
    print(data)