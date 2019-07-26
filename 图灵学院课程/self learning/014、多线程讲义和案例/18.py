import threading
import time

class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)


        if mutex.acquire(1):
            num = num+1
            msg = self.name+' set num to '+str(num)
            print(msg)
            mutex.acquire()
            mutex.release()
            mutex.release()

num = 0

mutex = threading.RLock()#可重复锁


def Th():#注意取函数名不能取test
    for i in range(5):
        t = MyThread()
        t.start()



if __name__ == '__main__':
    Th()