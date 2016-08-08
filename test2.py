import datetime
import time

current_timestamp=datetime.datetime.fromtimestamp(time.time()).strftime('%m_%d_%Y_%H_%M_%S')
logFile=open('C:/WalmartStockResults/log/loFile_'+current_timestamp+'.txt', 'w')

print str("hello")
print >>logFile, str("Helloworld")
logFile.close()
