#!/usr/bin/env python

import sys

def iterative_factorial(n):
    product = 1
    for i in range(2,n+1):
        product *= i
    return product

print iterative_factorial(int(sys.argv[1]))