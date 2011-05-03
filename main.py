#!/usr/bin/python2

from pypixel    import *

from util       import *
from window     import Window

title("cakewm test program")
show()

binds = {
}

for key, func in binds.iteritems():
    bind(key, func)

while True:
    update()
    clear()

pause()
