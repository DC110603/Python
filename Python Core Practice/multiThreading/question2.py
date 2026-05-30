"""Write a Python program that creates three separate threads where each
thread prints numbers from 1 to 5, and every printed number must be prefixed
with the name of the thread that printed it, such as “Thread-1: 3”."""

from threading import Thread
import time

def display(name, delay):
    for i in range(1, 6):
        time.sleep(delay)
        print(f"{name}: {i}")

t1 = Thread(target=display, args=("Thread-1", 2))
t2 = Thread(target=display, args=("Thread-2", 3))
t3 = Thread(target=display, args=("Thread-3", 1))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All threads finished")