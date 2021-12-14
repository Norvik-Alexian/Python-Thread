# Create 2 threads: 1. performing some action; 2. running with message in 15 seconds.
from threading import Thread
from time import sleep


def perform():
    print("Program is Started")


def print_current_second():
    sleep(15)
    print("15 Seconds is passed")


thread1 = Thread(target=perform)
thread2 = Thread(target=print_current_second)
thread1.start()
thread2.start()
