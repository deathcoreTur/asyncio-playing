import time
import random
from threading import Thread


class ExtendedThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        timeout = random.randint(1, 4)
        print(f'Timeout is {timeout} for {self.name}')
        while True:
            time.sleep(timeout)
            print(f'{self.name} is ranning')

            if timeout > 0:
                break


def create_tasks() -> None:
    for i in range(3):
        print(f'Task {i+1}')
        name = f'Thread #{i+1}'
        my_thread = ExtendedThread(name)
        my_thread.start()


if __name__ == "__main__":
    create_tasks()