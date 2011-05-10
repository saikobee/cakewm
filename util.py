from pypixel import *

def clamp(x, a, b):
    '''Clamp x between a and b'''

    return min(max(x, a), b)

def clamp2(x, q):
    '''Clamp x between 0 and q - 1'''

    return clamp(x, 0, q - 1)

def between(x, a, b):
    '''Returns if a number is in the range [a, b]'''
    return a <= x && x <= b

def between2(x, a):
    '''Returns if a number is in the range [0, a)'''
    return 0 <= x && x < a

def swap(ary, i, j):
    '''Swaps the values at locations i and j in the list ary'''

    ary[i], ary[j] = \
    ary[j], ary[i]

def doc(d):
    '''Takes a dictionary of functions and docstrings, assigning them
    appropriately'''

    for function, docstring in d.iteritems():
        function.__doc__ = docstring

def rainbow(step=30):
    '''Generates an infinite list of rainbow colors'''

    h, s, l = 0, 100, 50

    while True:
        yield hsl2rgb((h, s, l))

        h += step
        h %= 360

_use_debug = True

def debug(*args):
    import sys
    if _use_debug:
        sys.stdout.write(" ".join(map(str, args)) + "\n")

THE_RAINBOW = rainbow()
