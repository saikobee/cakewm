class Const(object):
    def __init__(self, num):
        self.num = num

    def __cmp__(self, that):
        return self.num - that.num

NEXT = Const(+1)
CUR  = Const( 0)
PREV = Const(-1)
