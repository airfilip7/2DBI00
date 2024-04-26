from types import FunctionType
from datetime import datetime as dt


def show_result(f: FunctionType):
    def wrapper(*args, **kwargs):
        module_name = f.__module__.split(".")[2]
        ch_name = module_name[0].upper() + module_name[-1]

        print(f"{dt.now().strftime('%H:%M:%S')} [{ch_name}] Exercise {f.__name__[-1]}")
        if f.__code__.co_argcount:
            f(*args, **kwargs)
        else:
            f()
        print()

    return wrapper


def print_matrix(M):
    for row in M:
        for i, cell in enumerate(row):
            print(cell, end=" " if i != len(row) - 1 else "\n")
    print()
