from util import *

from container import Container

class Display(Container):
    "A display manages screens"

    NAME = "Dpy"

    @property
    def screens(self):
        return self.items

    move_win_screen_num = Container.move_win_num
    select_screen_num   = Container.select_num

    def swap_tags_num(self, number):
        "Swap the current tags on the current and nth screen"

        try:
            this_screen = self.screens[self.cur]
            that_screen = self.screens[number  ]

            if (this_screen is not None and
                that_screen is not None):
                this_tag_num = this_screen.cur
                that_tag_num = that_screen.cur
                that_tag     = that_screen.item()
                this_tag     = this_screen.item()

                if (this_tag_num is not None and
                    that_tag_num is not None):
                    this_screen.items[this_tag_num] = that_tag
                    that_screen.items[that_tag_num] = this_tag
        except IndexError:
            debug("Screen out of range")
