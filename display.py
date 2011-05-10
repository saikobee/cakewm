import const

class Display(object):
    "A display manages all the screens for an X server"

    def __init__(self, **kwargs):
        self.cur     = kwargs.get("cur",     None)
        self.screens = kwargs.get("screens", [])

    def move_win_screen(self, direction):
        "Moves the current window to next/prev screen"

        win = self.take_cur_win()
        if win is not None:
            screen = self.get_screen(direction)
            if screen is not None:
               screen.add_window(win)

    def swap_tags(self, direction):
        "Swap the current tags on the current and next/prev screen"

        this_screen = self.get_screen(const.CUR)
        that_screen = self.get_screen(direction)

        if (this_screen is not None and
            that_screen is not None):

            this_tag = this_screen.get_tag(const.CUR)
            that_tag = that_screen.get_tag(const.CUR)

            this_screen.set_tag(that_tag)
            that_screen.set_tag(this_tag)

    def get_screen(self, direction):
        "Returns the cur/next/prev screen, or None if there isn't one"

        if self.cur is None:
            return None
        else:
            index = clamp(self.cur + direction.num, self.num_screens())
            return self.screens[index]

    def num_screens(self):
        "Returns the number of screens for this display"

        return len(self.screens)
