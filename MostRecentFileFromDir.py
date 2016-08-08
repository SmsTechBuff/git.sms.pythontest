

logdir='C:/WalmartStockResults/ItemFile/' # path to your log directory

logfiles = sorted([ f for f in os.listdir(logdir) if f.startswith('itemfile_')])

print "Most recent file = %s" % (logfiles[-1],)