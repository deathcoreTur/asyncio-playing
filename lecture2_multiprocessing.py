# import time
# import multiprocessing
# start = time.perf_counter()
#
#
# def please_sleep(n):
#     print(f"Sleeping for {n} seconds")
#     time.sleep(n)
#     print(f"Done Sleeping for {n} seconds")
#
#
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=please_sleep, args=[1])
#     p2 = multiprocessing.Process(target=please_sleep, args=[2])
#     p1.start()
#     p2.start()
#     finish = time.perf_counter()
#     print(f"Finished in {finish-start} seconds")

# -----------------------------------------------------
# import time
# import multiprocessing
# start = time.perf_counter()
#
#
# def please_sleep(n):
#     print(f"Sleeping for {n} seconds")
#     time.sleep(n)
#     print(f"Done Sleeping for {n} seconds")
#
#
# if __name__ == '__main__':
#     processes = []
#     for i in range(1, 6):
#         p = multiprocessing.Process(target=please_sleep, args=[i])
#         p.start()
#         processes.append(p)
#     for p in processes:
#         p.join()
#     finish = time.perf_counter()
#     print(f"Finished in {finish-start} seconds")
#
#     print(multiprocessing.cpu_count())

# -----------------------------------------------------

# import time
#
#
# def is_prime(n):
#     if n % 2 == 0:
#         return n == 2
#     d = 3
#     while d * d <= n and n % d != 0:
#         d += 2
#     return d * d > n
#
#
# start_time = time.time()
# for i in range(1, 10):
#     time.sleep(2)
#     str_prime = 'prime' if is_prime(i) else 'not a prime'
#     print(f'{i} is {str_prime} number')
# print(f'Time taken = {time.time() - start_time} seconds')

# --------------------------------------------------------------

# import time
# from multiprocessing import Process
#
#
# def is_prime(n):
#     if n % 2 == 0:
#         return n == 2
#     d = 3
#     while d * d <= n and n % d != 0:
#         d += 2
#     return d * d > n
#
#
# def multiprocessing_func(x):
#     time.sleep(2)
#     str_prime = 'prime' if is_prime(x) else 'not a prime'
#     print(f'{x} is {str_prime} number')
#
#
# if __name__ == '__main__':
#     start_time = time.time()
#     processes = []
#     for i in range(1, 10):
#         p = Process(target=multiprocessing_func, args=(i,))
#         processes.append(p)
#         p.start()
#
#     for process in processes:
#         process.join()
#
#     print(f'Time taken = {time.time() - start_time} seconds')

# --------------------------------------------------------------

# import time
# from multiprocessing import Pool
#
#
# def is_prime(n):
#     if n % 2 == 0:
#         return n == 2
#     d = 3
#     while d * d <= n and n % d != 0:
#         d += 2
#     return d * d > n
#
#
# def multiprocessing_func(x):
#     time.sleep(2)
#     str_prime = 'prime' if is_prime(x) else 'not a prime'
#     print(f'{x} is {str_prime} number')
#
#
# if __name__ == '__main__':
#     start_time = time.time()
#     pool = Pool()
#     pool.map(multiprocessing_func, range(1, 10))
#     pool.close()
#     print()
#     print('Time taken = {} seconds'.format(time.time() - start_time))

# --------------------------------------------------------------
# import time
# from multiprocessing import Process
#
#
# def non_daemon_process():
#     print("starting my Process")
#     time.sleep(8)
#     print("ending my Process")
#
#
# def daemon_process():
#     while True:
#         print("Hello")
#         time.sleep(2)
#
#
# if __name__ == '__main__':
#     non_daemon = Process(target=non_daemon_process, daemon=False)
#     daemon = Process(target=daemon_process, daemon=True)
#     daemon.start()
#     non_daemon.start()

# --------------------------------------------------------------
# import time
# import multiprocessing
#
#
# def child_process():
#    print('Starting function')
#    time.sleep(5)
#    print('Finished function')
#
#
# if __name__ == '__main__':
#     P = multiprocessing.Process(target=child_process)
#     P.start()
#     print("My Process has terminated, terminating main thread")
#     print("Terminating Child Process")
#     # P.join()
#     P.terminate()
#     print("Child Process successfully terminated")

# --------------------------------------------------------------
# import multiprocessing
#
#
# def child_process():
#    print("PID of Child Process is: {}".format(multiprocessing.current_process().pid))
#
#
# if __name__ == '__main__':
#     print("PID of Main process is: {}".format(multiprocessing.current_process().pid))
#     P = multiprocessing.Process(target=child_process)
#     P.start()
#     P.join()
#

# --------------------------------------------------------------
# from multiprocessing import Process
#
#
# class MyProcess(Process):
#     def __init__(self, ip, port):
#         Process.__init__(self)
#         self.ip = ip
#         self.port = port
#
#     def run(self):
#         print(f'called run method in process: {self.name} with ip: {self.ip} and port: {self.port}')
#
#
# if __name__ == '__main__':
#     jobs = []
#     for i in range(5):
#         port = f'808{i}'
#         P = MyProcess(ip='127.0.0.1', port=port)
#         jobs.append(P)
#         P.start()
#         P.join()

# --------------------------------------------------------------
# import time
# from multiprocessing import Process, Lock
#
#
# def printer(item, lock):
#     # lock.acquire()
#     try:
#         print(item)
#         time.sleep(2)
#     finally:
#         # lock.release()
#         pass
#
#
# if __name__ == '__main__':
#     lock = Lock()
#     items = ['tango', 'foxtrot', 10]
#
#     for item in items:
#         p = Process(target=printer, args=(item, lock))
#         p.start()

# --------------------------------------------------------------

# from multiprocessing import Process, Queue
#
#
# def creator(data, q):
#     print('Creating data and putting it on the queue')
#     for item in data:
#         q.put(item)
#
#
# def my_consumer(q):
#     while True:
#         data = q.get()
#         print('data found to be processed: {}'.format(data))
#         processed = data * 2
#         print(processed)
#         if q.empty():
#             break
#
#
# if __name__ == '__main__':
#     q = Queue()
#     data = [5, 10, 13, -1]
#     process_one = Process(target=creator, args=(data, q))
#     process_two = Process(target=my_consumer, args=(q,))
#     process_one.start()
#     process_two.start()
#     process_one.join()
#     process_two.join()

# --------------------------------------------------------------
# import multiprocessing
#
#
# def worker():
#     # print(id(LIST))
#     LIST.append('item')
#
#
# LIST = []
#
#
# if __name__ == "__main__":
#     processes = [
#         multiprocessing.Process(target=worker)
#         for _ in range(5)
#     ]
#     for p in processes:
#         p.start()
#     for p in processes:
#         p.join()
#     print(LIST)

# --------------------------------------------------------------
# USING MANAGER

# from multiprocessing import Process, Manager
#
# def dothing(L, i):  # the managed list `L` passed explicitly.
#     L.append("anything")
#
# if __name__ == "__main__":
#     with Manager() as manager:
#         L = manager.list()  # <-- can be shared between processes.
#         processes = []
#         for i in range(5):
#             p = Process(target=dothing, args=(L,i))  # Passing the list
#             p.start()
#             processes.append(p)
#         for p in processes:
#             p.join()
#         print (L)


from multiprocessing import Process, Manager


def worker(LIST, i):
    LIST.append(f'item {i}')


if __name__ == "__main__":
    with Manager() as manager:
        LIST = manager.list()  # <-- can be shared between processes.
        processes = [
           Process(target=worker, args=(LIST,i))
            for i in range(5)
        ]
        for p in processes:
            p.start()
        for p in processes:
            p.join()
        print(LIST)