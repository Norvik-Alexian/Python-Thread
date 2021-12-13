from threading import Thread
from time import sleep

rate = 3


def sleep_print():  # Sleep
    sleep(0.01)
    print("Something\n")


def volume(rate: int):
    volume = (4 * 3.14 * (rate ** 3)) // 3
    print(f"Volume of the Sphere is:", int(volume))


thread1 = Thread(target=sleep_print)
thread2 = Thread(target=volume, args=(rate,))

thread1.start()
thread1.join()

thread2.start()
thread2.join()