def clamp(x, a, b):
#   if   x < a: return a
#   elif x > b: return b
#   else:       return x

    return min(max(x, a), b)

def swap(ary, i, j):
  ary[i], ary[j] = \
  ary[j], ary[i]

def doc(d):
  for function, docstring in d.iteritems():
    function.__doc__ = docstring
