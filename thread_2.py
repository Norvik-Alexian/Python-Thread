# Create threads that will answer to each other.
from threading import Thread, current_thread

checker = True


def chat():
    thread_name = current_thread().name
    global checker
    if thread_name == "first thread" and checker:
        print("hello thread 2")
    elif thread_name == "first thread":
        print("again hello thread 2")

    if thread_name == "second thread" and checker:
        print("hello thread 1")
    elif thread_name == "second thread":
        print("again hello thread 1")
    checker = False


thread_1 = Thread(target=chat, name="first thread")
thread_2 = Thread(target=chat, name="second thread")

thread_2.start()
thread_1.start()