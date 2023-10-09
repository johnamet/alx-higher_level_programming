#!/usr/bin/python3


def no_c(my_string):
    m_str = ""

    for i in my_string:
        if i != "c" and i != "C":
            m_str += i

    return m_str
