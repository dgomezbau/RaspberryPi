from multiprocessing import Process
import time

def f(name):
    while True:
        print('hello', name)
        time.sleep(1)

def d(name):
    print('test2', name)
    time.sleep(2)
    print('test2', name)
    time.sleep(2)
    print('test2', name)
    time.sleep(2)
    print('test2', name)

if __name__ == '__main__':
    p1 = Process(target=f, args=('bob',))
    p2 = Process(target=d, args=('alice',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()




