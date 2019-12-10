import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name,counter, delay):
        threading.Thread.__init__(self)
        self.name=name
        self.counter= counter
        self.delay= delay
    def run(self):
        print ("The runing"+self.name)
        while self.counter:
            time.sleep(self.delay)
            print("%s: %s"%(self.name,time.ctime(time.time())))
            self.counter-=1
        print("Ket thuc",self.name)
try:
    threads=[]
    threa1= MyThread("threa1",10,2)
    threa2= MyThread("threa2",10,1)
    threa1.start()
    threa2.start()
    threads.append(threa1)
    threads.append(threa2)
    for t in threads:
        t.join()  
    print("ket thuc toan bo")
except:
    print("have error")