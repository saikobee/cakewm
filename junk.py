import util

from display    import Display
from screen     import Screen
from tag        import Tag
from column     import Column
from stack      import Stack
from window     import Window

@util.lazy
def mk(klass, func, num):
    return klass(cur=0, items=[func() for i in xrange(num)])

mk_stack    = mk(Stack,     Window,     1)
mk_col      = mk(Column,    mk_stack,   4)
mk_tag      = mk(Tag,       mk_col,     4)
mk_screen   = mk(Screen,    mk_tag,     9)
mk_display  = mk(Display,   mk_screen,  3)

display = mk_display()
