"""1.
Write a Python program that creates a worker thread which prints “Hello
from worker thread” while the main thread prints “Hello from main thread”, and
ensure that the main thread waits for the worker thread to finish execution
before the program exits.
"""

from  threading import Thread
import time

def worker():
    for i in range(5):
        time.sleep(3)
        print("Hello from worker thread")
def main():
    for i in range(5):
        time.sleep(2)
        print("Hello from main thread")

t1= Thread(target=worker)
t2= Thread(target=main)
t1.start()
t2.start()
t1.join()
t2.join()
print("Thread 1 finished execution")
print("Thread 2 finished execution")