class Screen(object):
    "A screen manages the set of tags associated with a single screen"

    def __init__(self, **kwargs):
        self.cur  = kwargs.get("cur",  None)
        self.tags = kwargs.get("tags", [])

    def move_win_tag_num(self, number):
        "Moves the current window to the tag identified by the given number"

        if self.cur is not None:
            try:
                win = self.take_cur_win()
                if win is not None:
                    self.tags[self.cur].add_window(win)
            except IndexError:
                debug("Attempted to move window to non-existent tag")

    def select_tag_num(self, number):
        if between2(number, len(self.tags)):
            self.cur = number
