def _guard(function):
    def inner(self, *args, **kwargs):
        if self.cur_window is not None:
            return function(*args, **kwargs)

class Stack(object):
    def __init__(self, windows=[]):
        self.windows    = windows
        self.cur_window = None

    @_guard
    def _go(self, a):
        self.cur_window += a

    def go_next(self): self._go(+1)
    def go_prev(self): self._go(-1)
