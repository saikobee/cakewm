import sys
import itertools

import pypixel

# from conf import Conf

def clamp(x, a, b):
    '''Clamp x between a and b'''

    return min(max(x, a), b)

def clamp2(x, q):
    '''Clamp x between 0 and q - 1'''

    return clamp(x, 0, q - 1)

def between(x, a, b):
    '''Returns if a number is in the range [a, b]'''
    return a <= x and x <= b

def between2(x, a):
    '''Returns if a number is in the range [0, a)'''
    return 0 <= x and x < a

def swap(ary, i, j):
    '''Swaps the values at locations i and j in the list ary'''

    ary[i], ary[j] = \
    ary[j], ary[i]

def doc(d):
    '''Takes a dictionary of functions and docstrings, assigning them
    appropriately'''

    for function, docstring in d.iteritems():
        function.__doc__ = docstring

def lazy(f):
    '''Returns a new function with delayed execution

    Examples:
    class A(object):
        @util.lazy
        def add(x, y):
            print x + y

    obj = A()
    dispatcher = {
        "a": obj.add(1, 2),
        "b": obj.add(4, 9),
    }'''

    return lambda *args, **kwargs: lambda: f(*args, **kwargs)

_use_debug = True

def debug(*args):
    if _use_debug:
        prefix = "cakewm: "
        sys.stdout.write(
            prefix
            + " ".join(map(str, args))
            + "\n"
        )

def error(message):
    sys.stderr.write("cakewm: error: %s\n" % message)
    sys.exit(1)

INFINITE_RAINBOW = itertools.cycle(
    map(
        lambda hue: pypixel.hsl2rgb((hue, 50, 40)),
        xrange(0, 360, 20)
    )
)
