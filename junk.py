import util

from containers.display    import Display
from containers.screen     import Screen
from containers.tag        import Tag
from containers.column     import Column
from containers.stack      import Stack

from window import Window

@util.lazy
def mk(klass, func, num):
    return klass(cur=0, items=[func() for i in xrange(num)])

mk_stack    = mk(Stack,     Window,     0)
mk_col      = mk(Column,    mk_stack,   1)
mk_tag      = mk(Tag,       mk_col,     1)
mk_screen   = mk(Screen,    mk_tag,     9)
mk_display  = mk(Display,   mk_screen,  1)

display = mk_display()
