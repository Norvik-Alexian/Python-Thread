# Create a thread, that continuously print some message after sleeping until the main thread finishes its execution.
from threading import Thread
from time import sleep


def message():
    print("Program Started")
    while True:
        sleep(1)
        print("Program in execution")


def main():
    sleep(10)
    print("Program Ended")


thread1 = Thread(target=message, daemon=True)
thread1.start()
sleep(3)
print('3 Seconds Sleep Ended')

