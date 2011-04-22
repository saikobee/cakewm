from pypixel import *

def clamp(x, a, b):
    '''Clamp x between a and b'''

    return min(max(x, a), b)

def clamp2(x, q):
    '''Clamp x between 0 and q - 1'''

    return clamp(x, 0, q - 1)

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


THE_RAINBOW = rainbow()
