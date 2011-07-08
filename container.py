import util
from window import Window

class Container(object):
    '''This is the base class for the various containers
    (Display, Screen, Tag, Column, Stack)'''

    NAME = "Cntr"

    def __init__(self, **kwargs):
        super(Container, self).__init__()
        self.cur    = kwargs.get("cur",     0)
        self.items  = kwargs.get("items",   [])

    def n_wins(self):
        return sum(map(lambda item: item.n_wins(), self.items))

    def fix_cur(self):
        if self.n_items() == 0:
            self.cur = None
        else:
            self.cur = util.clamp2(self.cur, self.n_items())

    def move_win_next(self): self.move_win_num((self.cur or 0) + 1)
    def move_win_prev(self): self.move_win_num((self.cur or 0) - 1)

    def _with_item(self, func):
        item = self.item()
        if item is None: return item
        else:            return func(item)

    def cur_win_title(self): return self._with_item(lambda item: item.cur_win_title())
    def cur_screen(self):    return self._with_item(lambda item: item.cur_screen())
    def tot_screens(self):   return self._with_item(lambda item: item.tot_screens())
    def cur_tag(self):       return self._with_item(lambda item: item.cur_tag())
    def tot_tags(self):      return self._with_item(lambda item: item.tot_tags())
    def cur_win(self):       return self._with_item(lambda item: item.cur_win())
    def tot_wins(self):      return self._with_item(lambda item: item.tot_wins())

    def move_win_num(self, number):
        "Moves the current window to nth screen"

        if self.cur is not None:
            if util.between2(number, self.n_items()):
                win = self.take_cur_win()
                if win is not None:
                    self.items[number].add_win(win)
                    self.select_num(number)
            else:
                util.debug("Out of range")

    def item(self):
        try:
            return self.items[self.cur]
        except (TypeError, IndexError):
            return None

    def n_items(self):
        return len(self.items)

    def select_next(self): self.select_num((self.cur or 0) + 1)
    def select_prev(self): self.select_num((self.cur or 0) - 1)

    def select_num(self, number):
        if util.between2(number, self.n_items()):
            self.cur = number
        else:
            util.debug("Out of range")

    def take_cur_win(self):
        item = self.item()
        return item.take_cur_win()

    def add_win(self, win):
        item = self.item()
        return item.add_win(win)

    def __str__(self):
        return "%s:%s:[%s]" % (
            type(self).NAME,
            self.cur,
            ", ".join(map(str, self.items))
        )
