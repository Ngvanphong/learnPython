import threading
import time
class Account:
    def __init__(self, name, accountTotal):
        self.accountTotal= accountTotal
        self.name= name

def withdraw(account , amount):
    locking.acquire()
    for i in range(10):
        if account.accountTotal>= amount:
            account.accountTotal-=amount
            print("so du",account.name, account.accountTotal)
        else:
            print ("Tai khoan het tien")
        time.sleep(1)
    locking.release()    
a1= Account("tai khoan1",6000)
locking= threading.Lock()
t1=threading.Thread(target=withdraw,args=(a1,1000))
t2=threading.Thread(target=withdraw,args=(a1,2000))
t1.start()
t2.start()