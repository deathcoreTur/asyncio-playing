import asyncio
import datetime


async def task(name: str, timeout: int, message: str) -> None:
    print('*'*50)
    start = datetime.datetime.now()

    print(f'Run {name} \t Start: {start} \t Timeout is {timeout}')
    while True:
        await asyncio.sleep(timeout)
        print(f'{message} from task # {name}')
        if timeout > 0:
            break

    end = datetime.datetime.now()
    print(f'End: {end}, \t Executed: {end - start}')


if __name__ == "__main__":
    print('Asynchronous!!!')
    tasks_async = [
        task('Task 1', 2, 'Hello'),
        task('Task 2', 1, 'Hello'),
        task('Task 3', 3, 'Hello'),
    ]
    asyncio.run(asyncio.wait(tasks_async))

    print('Synchronous!!!')
    tasks_sync = [
        task('Task 1', 2, 'Hello'),
        task('Task 2', 1, 'Hello'),
        task('Task 3', 3, 'Hello'),
    ]

    async def main(task, tasks):
        for task in tasks:
            try:
                await asyncio.wait_for(task, timeout=None)
            except asyncio.TimeoutError:
                print('timeout!')

    asyncio.run(main(task, tasks_sync))

    # tasks_infinite = [
    #     task('Task 1', 2, 'Hello'),
    #     task('Task 2', 0, 'Hello'),
    #     task('Task 3', 3, 'Hello'),
    # ]
    #
    #
    # async def wrap(tasks):
    #     for task in tasks:
    #         await asyncio.ensure_future(task)
    #
    # asyncio.run(wrap(tasks_infinite))
