#!/usr/bin/python2

from pypixel    import *

from util       import *

from display    import Display
from screen     import Screen
from tag        import Tag
from column     import Column
from stack      import Stack
from window     import Window

from cake.wm    import WM

title("cakewm test program")
show()

display = \
Display(
    cur=0,
    screens=[
        Screen(
            cur=0,
            tags=[
                Tag(
                    cur=0,
                    cols=[
                        Column(
                            cur=0,
                            stacks=[
                                Stack(
                                    cur=0,
                                    windows=[
                                        Window(),
                                        Window(),
                                        Window(),
                                    ]
                                )
                            ]
                        ),
                    ]
                ),
            ]
        ),
    ]
)

wm = WM(display)

binds = {
}

for key, func in binds.iteritems():
    bind(key, func)

while True:
    wm.organize()
    update()
    clear()

pause()
