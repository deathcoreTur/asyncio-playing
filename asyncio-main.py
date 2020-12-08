import random
import asyncio
from time import sleep


def task(number: int, message: str) -> None:
    timeout = random.randint(0, 2)
    print(f'Timeout is {timeout}')
    sleep(timeout)
    print(f'{message} from task # {number}')


def synchronous(message: str) -> None:
    for i in range(1, 4):
        task(i, message)


async def task_async(number: int, message: str) -> None:
    timeout = random.randint(1, 5)
    print(f'Timeout is {timeout} for task {number}')

    while True:
        await asyncio.sleep(timeout)
        print(f'{message} from task # {number}')

        if timeout > 0:
            break


async def asynchronous(message: str) -> None:
    tasks = [asyncio.ensure_future(task_async(i, message)) for i in range(1, 4)]
    await asyncio.wait(tasks)


if __name__ == "__main__":
    synchronous('Synchronous')

    print('*'*50)

    ioloop = asyncio.get_event_loop()
    ioloop.run_until_complete(asynchronous('Asynchronous'))
    ioloop.close()