import time, os
from multiprocessing import Process


def f(name):
    print(f'Hello, {name}. PID: {os.getpid()}')

if __name__ == '__main__':
    pr = Process(target=f, args=('Bob',))
    pr.start()
    pr.join()