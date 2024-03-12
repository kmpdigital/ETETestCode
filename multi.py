"""
!!!!THIS CODE WILL NOT RUN IN JUPYTER!!!
You need to run this in terminal or another IDE
"""
from multiprocessing import Process, Pipe


class CustomClass:
    pass


def work(connection):
    while True:
        instance = connection.recv()

        if instance:
            print(
                "CHLD: recv: {}".format(instance)
            )

        else:
            return


def main2():
    parent_conn, child_conn = Pipe()
    parent_conn, child_conn2 = Pipe()
    child = Process(target=work, args=(child_conn,))
    child2 = Process(target=work, args=(child_conn2,))


    for item in (
        42,
        'some string',
        {'one': 1},
        CustomClass(),
    ):
        print(
            "PRNT: send: {}".format(item)
        )
        parent_conn.send(item)

    child.start()
    child.join()
    child2.start()
    child2.join()

def main():
    import multiprocessing as mp
    import random

    val = random.random()

def simple_func(val):
    print(val)


if __name__ == '__main__':
    #main()
    print('Before multiprocessing: ')
    simple_func(val)
    print('After multiprocessing:')
    p = mp.Process(target=simple_func, args = val)
    p.start()
    p.join()
#if __name__ == "__main__":
#    main()