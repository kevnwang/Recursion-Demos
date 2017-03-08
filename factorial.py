#!/usr/bin/env python

import sys 

def factorial(n):
    # print "push: factorial(" + str(n) + ")"
    if n <= 1:
        # print "start popping"
        return n
    else:
        product = n * factorial(n-1)
        # print "pop: " + str(n) + " * factorial(" + str(n - 1) + ") = " + str(product)
        return product

print factorial(int(sys.argv[1]))