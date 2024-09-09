import sys
import typing


def add(p1: int, p2: int) -> int:
    return p1 + p2


param1 = int(sys.argv[1])
param2 = int(sys.argv[2])

print(add(param1, param2))
