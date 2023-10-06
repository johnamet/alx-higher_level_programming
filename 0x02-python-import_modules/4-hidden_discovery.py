#!/usr/bin/python3
"""Prints all the names defined by the compiled module hidden_4.pyc."""

import dis
import importlib.util
import sys


def print_names():
    """Prints all the names defined by the compiled module hidden_4.pyc."""
    spec = importlib.util.spec_from_file_location("hidden_4", "./hidden_4.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for name in dir(module):
        if not name.startswith("__"):
            print(name)


if __name__ == "__main__":
    sys.dont_write_bytecode = True
    print_names()

