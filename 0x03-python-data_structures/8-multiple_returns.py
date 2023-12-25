#!/usr/bin/python3


def multiple_returns(sentence):
    len_sent = len(sentence)
    first_char = None if len_sent == 0 else sentence[0]

    tuple_sent = (len_sent, first_char)

    return tuple_sent
