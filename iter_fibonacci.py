#!/usr/bin/env python

import sys 

def iterative_fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

print iterative_fibonacci(int(sys.argv[1]))