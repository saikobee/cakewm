import os
import sys
import itertools

import pypixel

# from conf import Conf

def clear():
    "Clear the screen"

    os.system("clear")

def echo(*args):
    "print wrapper"

    print " ".join(map(str, args))

def invert_dict(d):
    return dict((v,k) for k in d for v in d[k])

def rgb_assert(rgb):
    bad_val      = lambda val: not (0 <= val <= 255)
    any_bad_vals = any(map(bad_val, rgb))
    if any_bad_vals:
        color_error()

def hsl_assert(hsl):
    h, s, l  = hsl
    good_h   = 0 <= h <= 360
    good_s   = 0 <= s <= 100
    good_l   = 0 <= l <= 100
    all_good_vals = all((good_h, good_s, good_l))
    if not all_good_vals:
        color_error()

# The ranges and order are the same for HSL and HSV colors
hsv_assert = hsl_assert

def color_error():
    errors(
        "Bad color value",
        "Hex colors must be 3 or 6 digits",
        "RGB colors must be in the range 0-255",
        "As for HSL and HSV colors,",
        "Hue must be in the range 0-360",
        "Saturation, lightness, and value must all be in the range 0-100"
    )

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

def debugs(*args):
    for arg in args: debug(arg)

def error(message):
    sys.stderr.write("cakewm: error: %s\n" % message)
    sys.exit(1)

def errors(message0, *messages):
    sys.stderr.write("cakewm: error: %s\n" % message0)
    # Pad out the subsequent messages
    spacing = "-" * len("error:")
    for message in messages:
        sys.stderr.write("cakewm: %s %s\n" % (spacing, message))
    sys.exit(1)

INFINITE_RAINBOW = itertools.cycle(
    map(
        lambda hue: pypixel.hsl2rgb((hue, 50, 40)),
        xrange(0, 360, 20)
    )
)
