import time, os

pid = os.getpid()

for i in range(5):
    print(pid, time.time())
    time.sleep(2)