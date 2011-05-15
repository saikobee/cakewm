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
mk_col      = mk(Column,    mk_stack,   2)
mk_tag      = mk(Tag,       mk_col,     2)
mk_screen   = mk(Screen,    mk_tag,     2)
mk_display  = mk(Display,   mk_screen,  2)

display = mk_display()
