from __future__ import annotations
import time
import random

import dask
from dask import delayed

import numpy as np

def increment (x: int | float) -> int | float:
    return x + 1

def double(x: int | float) -> int | float:
    return x * 2

def add (x: int | float, y: int | float) -> int | float:
    return x + y

data = [1, 2, 3, 4, 5]
output = []

for x in data:
    a = increment (x)
    b = double (x)
    c = add (a, b)
    output.append(c)

total = sum(output)

print(f"{total=}")

@delayed
def delayed_increment (x: int | float) -> int | float:
    return x + 1

@delayed
def delayed_double(x: int | float) -> int | float:
    return x * 2

@delayed
def delayed_add (x: int | float, y: int | float) -> int | float:
    return x + y

data = [1, 2, 3, 4, 5]
delayed_output = []

for x in data:
    a = delayed_increment (x)
    b = delayed_double (x)
    c = delayed_add (a, b)
    delayed_output.append(c)

delayed_total = delayed(sum)(delayed_output)


print(f"{delayed_total.compute()=}")

delayed_total.visualize() 