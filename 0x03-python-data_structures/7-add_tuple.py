#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        new_tuple_a = tuple_a + (0, 0)
    else:
        new_tuple_a = tuple_a

    if len(tuple_b) < 2:
        new_tuple_b = tuple_b + (0, 0)
    else:
        new_tuple_b = tuple_b

    new_tuple = (new_tuple_a[0] + new_tuple_b[0],
                 new_tuple_a[1] + new_tuple_b[1])
    return new_tuple
