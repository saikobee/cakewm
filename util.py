def clamp(x, a, b):
    '''Clamp x between a and b'''

    return min(max(x, a), b)

def swap(ary, i, j):
    '''Swaps the values at locations i and j in the list ary'''

    ary[i], ary[j] = \
    ary[j], ary[i]

def doc(d):
    '''Takes a dictionary of functions and docstrings, assigning them
    appropriately'''

    for function, docstring in d.iteritems():
        function.__doc__ = docstring

def guard(func1):
    '''Guard function generator'''

    def guard2(func2):
        def inner(self, *args, **kwargs):
            if func1(self) is not None:
                return func2(*args, **kwargs)

    return guard2
