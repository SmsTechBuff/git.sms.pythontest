import urllib

target_url="http://userquote.com/tools/record.txt"
response = urllib.urlopen(target_url)
data = response.readlines()

walmart_item_number=[]
for line in data:
    #print line
    words =line.split(",")
    if len(words)>2 :
        if words[0]== "WALMART":
            print words[0],"->",words[1]  
            walmart_item_number.append(words[1].strip())  
        
print len(walmart_item_number)

walmart_item_number=list(set(walmart_item_number))

print len(walmart_item_number)

for item in walmart_item_number:
    print item