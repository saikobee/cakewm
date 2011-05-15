class Container(object):
    '''This is the base class for the various containers
    (Display, Screen, Tag, Column, Stack)'''

    def __init__(self, **kwargs):
        self.cur    = kwargs.get("cur",     0)
        self.items  = kwargs.get("items",   [])

    def move_win_num(self, number):
        "Moves the current window to nth screen"

        if self.cur is not None:
            try:
                win = self.take_cur_win()
                if win is not None:
                    self.items[self.cur].add_window(win)
            except IndexError:
                debug("Attempted to move window to non-existent container")

    def item(self):
        try:
            return self.items[self.cur]
        except (TypeError, IndexError):
            return None

    def __repr__(self):
        return "C:%s:[%s]" % (
            self.cur,
            ", ".join(map(str, self.items))
        )
