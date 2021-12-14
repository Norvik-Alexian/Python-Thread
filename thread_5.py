# Create a thread pool with couples of threads running several tasks.
from concurrent.futures import ThreadPoolExecutor
from time import sleep

excutor = ThreadPoolExecutor(max_workers=4)


def print_message():
    sleep(2)
    print('This is a message from ThreadPool!')


for _ in range(10):
    excutor.submit(print_message)
