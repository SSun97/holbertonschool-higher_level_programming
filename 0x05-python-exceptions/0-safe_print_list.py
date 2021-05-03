#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0

    try:
        for i in range(x):
            n = n + 1
            print(my_list[i], end='')
        print()
        return n
    except IndexError:
        print()
        return n - 1
