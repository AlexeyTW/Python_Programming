import time, os
from multiprocessing import Process
from threading import Thread
from queue import Queue


def f(name):
    print(f'Hello, {name}. PID: {os.getpid()}')


def count(n):
    while n > 0:
        n -= 1


def worker(q: Queue, n):
    while True:
        item = q.get()
        if item is None:
            break
        print('process data: ', n, item)


#if __name__ == '__main__':
    '''pr = Process(target=f, args=('Jane',))
    pr.start()
    pr.join()'''

class PrintProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f'Hello, {self.name}. PID = {self.pid}')

#if __name__ == '__main__':
    '''p = PrintProcess('Mike')
    p.start()
    p.join()'''

'''th = Thread(target=f, args=('Thread Name',))
th.start()
th.join()'''

class PrintThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f'Hello, {self.name}. PID = {os.getpid()}')

'''th = PrintThread('Michael')
th.start()
th.join()'''

t0 = time.time()
count(100_000_000)
count(100_000_000)
t1 = time.time()
print(t1 - t0)

t0 = time.time()
th1 = Thread(target=count, args=(100_000_000,))
th2 = Thread(target=count, args=(100_000_000,))

th1.start(); th2.start()
th1.join(); th2.join()

print(time.time() - t0)