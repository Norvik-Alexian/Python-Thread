# Create 2 threads sharing some variable, modifying it and implement Synchronization.
from threading import Thread
from time import sleep

x = 0


def increment():
    global x
    sleep(0.5)
    x += 1


def decrement():
    global x
    sleep(1)
    x -= 1


def thread1():
    for i in range(5):
        increment()
        print("*" * 2 * x)


def thread2():
    global x
    for i in range(5):
        decrement()
        print("*" * 2 * x)


def trigger():
    t1 = Thread(target=thread1())
    t2 = Thread(target=thread2())

    t1.start()
    t2.start()

    t1.join()
    t2.join()


for s in range(4):
    print(f"Sequence", {s+1})
    trigger()