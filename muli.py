"""
"Multiprocessing" section example showing how
to create new processes with `multiprocessing` module
"""
from multiprocessing import Process
import os


def work(identifier):
    print(
        'Process {}, pid: {}'
        ''.format(identifier, os.getpid())
    )


def main():
    processes = [
        Process(target=work, args=(number,))
        for number in range(5)
    ]
    for process in processes:
        process.start()

    while processes:
        processes.pop().join()


if __name__ == "__main__":
    main()