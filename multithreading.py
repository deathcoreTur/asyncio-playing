# import time
# from threading import Thread
#
#
# def sleepMe(i):
#     print(f"Поток {i} засыпает на 5 секунд.\n")
#     time.sleep(5)
#     print(f"Поток {i} сейчас проснулся.\n")
#
#
# for i in range(10):
#     th = Thread(target=sleepMe, args=(i, ))
#     th.start()

# ----------------------------------------------------
# import time
# import random
#
#
# def sleepMe(i):
#     # sleep = random.randint(0,2)
#     print(f"Задача {i} засыпает на {1} секунду.\n")
#     time.sleep(1)
#     print(f"Задача {i} сейчас проснулся.\n")
#
#
# for i in range(10):
#     sleepMe(i)


# -----------------------------------------------------

# import time
# import threading
# from threading import Thread
#
#
# def sleepMe(i):
#     print(f"Поток {i} засыпает на 5 секунд.")
#     time.sleep(5)
#     print(f"Поток {i} сейчас проснулся.")
#
#
# for i in range(10):
#     th = Thread(target=sleepMe, args=(i, ))
#     th.start()
#     print(f"Запущено потоков: {threading.active_count()}.")

# -----------------------------------------------------
# import time
# import threading
# from threading import Thread
#
#
# def sleepMe(i, test):
#     print(f"Поток {threading.current_thread()} засыпает на 5 секунд.  {test}\n")
#     time.sleep(5)
#     print(f"Поток {threading.current_thread()} сейчас проснулся.")
#
#
# # Cоздаем только четыре потока
# for i in range(4):
#     test= 'sssss'
#     th = Thread(name=f'Test {i}', target=sleepMe, args=(i, test))
#     th.start()


# -----------------------------------------------------

# import logging
# import threading
# import time
#
#
# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)
#
#
# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")
#     logging.info("Main    : before creating thread")
#     x = threading.Thread(target=thread_function, args=(1,))
#     logging.info("Main    : before running thread")
#     x.start()
#     logging.info("Main    : wait for the thread to finish")
#     x.join()
#     logging.info("Main    : all done")

# -----------------------------------------------------

# import logging
# import threading
# import time
#
#
# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)
#
#
# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")
#     logging.info("Main    : before creating thread")
#     x = threading.Thread(target=thread_function, args=(1,), daemon=True)
#     logging.info("Main    : before running thread")
#     x.start()
#     logging.info("Main    : wait for the thread to finish")
#     # x.join()
#     logging.info("Main    : all done")

# -----------------------------------------------------

# import threading
# import datetime
#
#
# class myThread (threading.Thread):
#    def __init__(self, name, counter):
#        threading.Thread.__init__(self)
#        self.threadID = counter
#        self.name = name
#        self.counter = counter
#
#    def run(self):
#        print("Starting " + self.name)
#        print_date(self.name, self.counter)
#        print("Exiting " + self.name)
#
#
# def print_date(threadName, counter):
#     today = datetime.datetime.now()
#     print(
#         "%s[%d]: %s" % (threadName, counter, today)
#     )
#
#
# # Создать треды
# thread1 = myThread("Thread", 1)
# thread2 = myThread("Thread", 2)
#
# # Запустить треды
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
# print("Exiting the Program!!!")

# ----------------------------------------------------
# Without LOCK
# import threading
#
# x = 0
#
#
# def increment():
#     global x
#     x += 1
#
#
# def thread_task():
#     for _ in range(100000):
#         increment()
#
#
# def main_task():
#     global x
#     # setting global variable x as 0
#     x = 0
#
#     # creating threads
#     t1 = threading.Thread(target=thread_task)
#     t2 = threading.Thread(target=thread_task)
#
#     # start threads
#     t1.start()
#     t2.start()
#
#     # wait until threads finish their job
#     t1.join()
#     t2.join()
#
#
# if __name__ == "__main__":
#     for i in range(10):
#         main_task()
#         print(f"Iteration {i}: x = {x}")

# ----------------------------------------------------
# import threading
#
# # global variable x
# x = 0
#
#
# def increment():
#     global x
#     x += 1
#
#
# def thread_task(lock):
#     for _ in range(100000):
#         lock.acquire()
#         increment()
#         lock.release()
#
#
# def main_task():
#     global x
#     x = 0
#
#     # creating a lock
#     lock = threading.Lock()
#
#     # creating threads
#     t1 = threading.Thread(target=thread_task, args=(lock,))
#     t2 = threading.Thread(target=thread_task, args=(lock,))
#
#     # start threads
#     t1.start()
#     t2.start()
#
#     # wait until threads finish their job
#     t1.join()
#     t2.join()
#
#
# if __name__ == "__main__":
#     for i in range(10):
#         main_task()
#         print(f"Iteration {i}: x = {x}")

# ----------------------------------------------------
# Homework

import threading
import random
import time


def thread_job():
    global counter
    old_counter = counter
    time.sleep(random.randint(0, 1))
    counter = old_counter + 1
    print(f"{counter} ", end="")


counter = 0
threads = [threading.Thread(target=thread_job) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(f"finally counter: {counter}")

# ----------------------------------------------------
# Homework solution

# import threading
# import random
# import time
#
#
# def thread_job():
#     lock.acquire()  # mutex
#     global counter
#     old_counter = counter
#     time.sleep(random.randint(0, 1))
#     counter = old_counter + 1
#     print(f'{counter} ', end='')
#     lock.release()
#
#
# lock = threading.Lock()
# counter = 0
# threads = [threading.Thread(target=thread_job) for _ in range(10)]
# for thread in threads:
#     thread.start()
# for thread in threads:
#     thread.join()
# print(f'Finally counter {counter}')



















