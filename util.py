def clamp(x, a, b):
#   if   x < a: return a
#   elif x > b: return b
#   else:       return x

    return min(max(x, a), b)
