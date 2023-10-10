#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    
    l = 0
    r = 0

    if len(tuple_a) == 0:
        tuple_a = (0, 0)

    if len(tuple_b) == 0:
        tuple_b = (0, 0)

    if len(tuple_a) < 2:
        tuple_a = (tuple_a[0], 0)

    if len(tuple_b) < 2:
        tuple_b = (tuple_b[0], 0)

    if len(tuple_a) > 2:
        tuple_a = tuple_a[:2]

    if len(tuple_b) > 2:
        tuple_b = tuple_b[:2]

    l = tuple_a[0] + tuple_b[0]
    r = tuple_a[1] + tuple_b[1]

    tuple_c = (l, r)

    return tuple_c
