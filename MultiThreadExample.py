from threading import Thread
import time
import Queue
def str_to_int(arg, queue):
    result=arg
    queue.put({result})

def combine():
    arguments = ('49767337', '36483179', '37648910','38375872','44728585')
    BMSEEKURL="http://bmseek.tk/index.php?zip=40229&itemID="
    q = Queue.Queue()
    threads = []

    for argument in arguments:
        t = Thread(target=str_to_int, args=(BMSEEKURL+argument, q))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return [q.get() for _ in xrange(len(arguments))]

for ele in combine():
    print ele