import threading
import time
sum = 0
loopSum = 1000000


lock = threading.Lock()


def myAdd():
    global  sum, loopSum
    print("myAdd starting at:", time.ctime())
    for i in range(1, loopSum):
        # 上锁，申请令牌
        lock.acquire()
        sum += 1
        # 释放锁
        lock.release()
    time.sleep(4)
    print("myAdd ending at:", time.ctime())



def myMinu():
    print("myMinu starting at:", time.ctime())
    global  sum, loopSum
    for i in range(1, loopSum):
        lock.acquire()
        sum -= 1
        lock.release()
    time.sleep(2)
    print("myMinu ending at:", time.ctime())
if __name__ == '__main__':
    print("Starting ....{0}".format(sum))

    # 开始多线程的实例，看执行结果是否一样
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done .... {0}".format(sum))
