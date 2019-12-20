from multiprocessing import Process
import multiprocessing, ctypes
import time
import queue

'''def f(name):
    while True:
        print(name)
        time.sleep(1)'''

def d(name):
    print('test2', name)
    time.sleep(2)
    print('test2', name)
    time.sleep(2)
    print('test2', name)
    time.sleep(2)
    print('test2', name)

def f(q,name):
    q.put(name)


if __name__ == '__main__':

    q = queue.Queue()
    name = 'Carol'
    p1 = Process(target=f, args=(q, name))
    p1.start()
    print(q.get())
    time.sleep(2)
    name = ' Daniel'
    f(q,name)
    print(q.get())
    p1.join()
    print('Pasa')
    


