# from time import sleep
# from concurrent.futures import ThreadPoolExecutor
#
#
# def task(message):
#    sleep(2)
#    return message
#
#
# def task2(message):
#    sleep(1)
#    return message
#
#
# def main():
#    executor = ThreadPoolExecutor(5)
#    future = executor.submit(task, ("Completed"))
#    print(future.done())
#    sleep(3)
#    print(future.done())
#    print(future.result())
#
#    future2 = executor.submit(task2, ("Completed task 2"))
#    print(future2.done())
#    sleep(1)
#    print(future2.done())
#    print(future2.result())
#
#
# if __name__ == '__main__':
#     main()

# --------------------------------------------------------------
# from time import sleep
# from concurrent.futures import ThreadPoolExecutor
#
#
# def task(message):
#    sleep(2)
#    return message
#
#
# def main():
#    executor = ThreadPoolExecutor(5)
#    future = executor.submit(task, ("Completed"))
#    print(future.done())
#    sleep(2)
#    print(future.done())
#    print(future.result())
#
#
# if __name__ == '__main__':
#     main()

# --------------------------------------------------------

# import concurrent.futures
# import urllib.request
#
# URLS = ['http://www.foxnews.com/',
#    'http://www.cnn.com/',
#    'http://wsj.com/',
#    'http://www.bbc.com/',
#    'http://some-made-up-domain.com/']
#
#
# def load_url(url, timeout):
#    with urllib.request.urlopen(url, timeout=timeout) as conn:
#       return conn.read()
#
#
# with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#
#    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
#    for future in concurrent.futures.as_completed(future_to_url):
#       url = future_to_url[future]
#       try:
#          data = future.result()
#       except Exception as exc:
#          print(f'{url} generated an exception: {exc}')
#       else:
#          print(f'{url} page is {len(data)} bytes')

# --------------------------------------------------------
# import time
# from concurrent.futures import ThreadPoolExecutor
#
#
# def wait_on_future():
#     f = 3
#     time.sleep(4)
#     print(f)
#
#
# executor = ThreadPoolExecutor(max_workers=2)
# executor.submit(wait_on_future)
# executor.shutdown(wait=True)
#
# print("elo")

# ---------------------------------------------------------
# from concurrent.futures import ThreadPoolExecutor
#
# def wait_on_future():
#     f = 3
#     import time
#     time.sleep(4)
#     print(f)
#
# with ThreadPoolExecutor(max_workers=2) as executor:
#     executor.submit(wait_on_future)
# print("elo")

# ---------------------------------------------------------
# from concurrent.futures import ThreadPoolExecutor
#
#
# values = [2,3,4,5]
#
#
# def square(n):
#    return n * n
#
#
# def main():
#    with ThreadPoolExecutor(max_workers=3) as executor:
#       results = executor.map(square, values)
#       for result in results:
#             print(result)
#
#
# if __name__ == '__main__':
#    main()

# ---------------------------------------------------------
# from time import sleep
# from concurrent.futures import ProcessPoolExecutor
#
#
# def task(message):
#    sleep(1)
#    return message
#
#
# def main():
#    executor = ProcessPoolExecutor(5)
#    future = executor.submit(task, ("Completed"))
#    print(future.done())
#    sleep(2)
#    print(future.done())
#    print(future.result())
#
#
# if __name__ == '__main__':
#    main()

# -------------------------------------------
# import concurrent.futures
# import urllib.request
#
# URLS = ['http://www.foxnews.com/',
#    'http://www.cnn.com/',
#    'http://wsj.com/',
#    'http://www.bbc.co.uk/',
#    'http://some-made-up-domain.com/']
#
#
# def load_url(url, timeout):
#    with urllib.request.urlopen(url, timeout=timeout) as conn:
#       return conn.read()
#
#
# def main():
#    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
#       future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
#       for future in concurrent.futures.as_completed(future_to_url):
#          url = future_to_url[future]
#          try:
#             data = future.result()
#          except Exception as exc:
#             print('%r generated an exception: %s' % (url, exc))
#          else:
#             print('%r page is %d bytes' % (url, len(data)))
#
#
# if __name__ == '__main__':
#    main()

# --------------------------------------------------
# from concurrent.futures import ProcessPoolExecutor
#
# values = [2, 3, 4, 5]
#
#
# def square(n):
#    return n * n
#
#
# def main():
#    with ProcessPoolExecutor(max_workers=3) as executor:
#       results = executor.map(square, values)
#    for result in results:
#       print(result)
#
#
# if __name__ == '__main__':
#    main()

# --------------------------------------------------
# import time
# import concurrent.futures
#
# value = [8000000, 7000000]
#
#
# def counting(n):
#    start = time.time()
#    while n > 0:
#       n -= 1
#    return time.time() - start
#
#
# def main():
#    start = time.time()
#    with concurrent.futures.ProcessPoolExecutor() as executor:
#       for number, time_taken in zip(value, executor.map(counting, value)):
#          print('Start: {} Time taken: {}'.format(number, time_taken))
#    print('Total time taken: {}'.format(time.time() - start))
#
#
# if __name__ == '__main__':
#    main()

# # --------------------------------------------------
# import time
# import concurrent.futures
#
# value = [8000000, 7000000]
#
#
# def counting(n):
#    start = time.time()
#    while n > 0:
#       n -= 1
#    return time.time() - start
#
#
# def main():
#    start = time.time()
#    with concurrent.futures.ThreadPoolExecutor() as executor:
#       for number, time_taken in zip(value, executor.map(counting, value)):
#          print('Start: {} Time taken: {}'.format(number, time_taken))
#       print('Total time taken: {}'.format(time.time() - start))
#
#
# if __name__ == '__main__':
#    main()
# -----------------------------------------
# ASYNCIO
# import asyncio
#
#
# async def my_coro(delay):
#     loop = asyncio.get_running_loop()
#     end_time = loop.time() + delay
#     while True:
#         print("Blocking...")
#         await asyncio.sleep(1)
#         if loop.time() >= end_time:
#             print("Done.")
#             break
#
#
# async def main():
#     await my_coro(3)
#
#
# asyncio.run(main())
# -----------------------------------------

# import asyncio
# import time
# from datetime import datetime
#
#
# async def custom_sleep():
#     print('SLEEP', datetime.now())
#     time.sleep(1)
#
#
# async def factorial(name, number):
#     f = 1
#     for i in range(2, number+1):
#         print(f'Task {name}: Compute factorial({i})')
#         await custom_sleep()
#         f *= i
#     print(f'Task {name}: factorial({number}) is {f}\n')
#
#
# start = time.time()
# loop = asyncio.get_event_loop()
# tasks = [
#     asyncio.ensure_future(factorial("A", 3)),
#     asyncio.ensure_future(factorial("B", 4)),
# ]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
# end = time.time()
# print("Total time: {}".format(end - start))
# -----------------------------------------
# import asyncio
# import time
# from datetime import datetime
#
#
# async def custom_sleep():
#     print('SLEEP {}\n'.format(datetime.now()))
#     await asyncio.sleep(1)
#
#
# async def factorial(name, number):
#     f = 1
#     for i in range(2, number+1):
#         print(f'Task {name}: Compute factorial({i})')
#         await custom_sleep()
#         f *= i
#     print(f'Task {name}: factorial({number}) is {f}\n')
#
#
# start = time.time()
# loop = asyncio.get_event_loop()
# tasks = [
#     asyncio.ensure_future(factorial("A", 3)),
#     asyncio.ensure_future(factorial("B", 4)),
# ]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
# end = time.time()
# print("Total time: {}".format(end - start))

# -------------------------------------------------
#
# def basic_coroutine1(start):
#     print('Start value:', start)
#     first = yield
#     print('First received:', first)
#     second = yield
#     print('Second received:', second)
#
#
# bc1 = basic_coroutine1(100)
# next(bc1)
# # bc1.send(None)
#
# bc1.send(200)
#
# bc1.send(300)

# -------------------------------------------------

# def basic_coroutine2():
#     collection = []
#     while True:
#         item = yield
#         if item is None:
#             return collection
#         collection.append(item)
#
#
# bc2 = basic_coroutine2()
# next(bc2)
# bc2.send(100)
# bc2.send(200)
# bc2.send(300)
#
# try:
#     bc2.send(None)
# except StopIteration as e:
#     result = e.value
#     print(result)

# -------------------------------------------------
# def basic_coroutine3(items):
#     collection = [i for i in items]
#     print('inizialization')
#     while True:
#         print('return collection')
#         item = yield collection
#         print(f'get new item {item}')
#         collection.append(item)
#
#
# bc3 = basic_coroutine3([1, 2, 3])
# print(next(bc3))
#
# print(bc3.send(100))
#
# print(bc3.send(200))
#
# bc3.close()
#
# bc3.send(400)

# -------------------------------------------------
#
# from math import sqrt
# import time
#
#
# def is_prime(x):
#     print(f'Processing {x}...')
#
#     if x < 2:
#         print(f'{x} is not a prime number.')
#
#     elif x == 2:
#         print(f'{x} is a prime number.')
#
#     elif x % 2 == 0:
#         print(f'{x} is not a prime number.')
#
#     else:
#         limit = int(sqrt(x)) + 1
#         for i in range(3, limit, 2):
#             if x % i == 0:
#                 print(f'{x} is not a prime number.')
#                 return
#
#         print(f'{x} is a prime number.')
#
#
# if __name__ == '__main__':
#     start = time.time()
#     is_prime(9637529763296797)
#     is_prime(427920331)
#     is_prime(157)
#     print(f'time: {time.time() - start}')

# -------------------------------------------------
from math import sqrt
import asyncio
import time

# Для улучшения отзывчивости мы бы хотели переключать
# задачи на протяжнии своей большой задачи и не делать
# этого в маленькой задаче. Такая настройка позволит
# нашим средней и малой задачам стартовать, выполняться,
# а может быть даже и завершиться во время исполнения
# самой большой задачи
# async def is_prime(x):
#     print(f'Processing {x}...')
#
#     if x < 2:
#         print(f'{x} is not a prime number.')
#
#     elif x == 2:
#         print(f'{x} is a prime number.')
#
#     elif x % 2 == 0:
#         print(f'{x} is not a prime number.')
#
#     else:
#         limit = int(sqrt(x)) + 1
#         for i in range(3, limit, 2):
#             if x % i == 0:
#                 print(f'{x} is not a prime number.')
#                 return
#             elif i % 100000 == 1:
#                 await asyncio.sleep(0)
#
#         print(f'{x} is a prime number.')
#
#
# # нам требуется преобразовать и функцию is_prime(),
# # и функцию main() в сопрограммы
# async def main():
#
#     task1 = loop.create_task(is_prime(9637529763296797))
#     task2 = loop.create_task(is_prime(427920331))
#     task3 = loop.create_task(is_prime(157))
#
#     await asyncio.wait([task1, task2, task3])
#
#
# # мы создаём свой цикл событий и применяем
# # её для запуска своей сопрограммы main(),
# # пока она не завершит своего исполнения
# try:
#     start = time.time()
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
# except Exception as e:
#     print('There was a problem:')
#     print(str(e))
# finally:
#     print(f'time: {time.time() - start}')
#     loop.close()

# ----------------------------------------
from math import sqrt
import asyncio
from concurrent.futures import ProcessPoolExecutor
import time


# async def is_prime(x):
def is_prime(x):
    print(f'Processing {x}...')

    if x < 2:
        print(f'{x} is not a prime number.')

    elif x == 2:
        print(f'{x} is a prime number.')

    elif x % 2 == 0:
        print(f'{x} is not a prime number.')

    else:
        limit = int(sqrt(x)) + 1
        for i in range(3, limit, 2):
            if x % i == 0:
                print(f'{x} is not a prime number.')
                return

        print(f'{x} is a prime number.')


async def main():
    task1 = loop.run_in_executor(executor, is_prime, 9637529763296797)
    task2 = loop.run_in_executor(executor, is_prime, 427920331)
    task3 = loop.run_in_executor(executor, is_prime, 157)

    await asyncio.gather(*[task1, task2, task3])


if __name__ == '__main__':
    try:
        start = time.time()

        executor = ProcessPoolExecutor(max_workers=3)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())

        print(f'Took {time.time() - start} seconds.')

    except Exception as e:
        print('There was a problem:')
        print(str(e))

    finally:
        loop.close()
