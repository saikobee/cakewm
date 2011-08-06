import util
import const
from   conf import conf

class Magic(object):
    '''The subclass must define get_max() as a static method and
    default_item() as an instance method'''

    def item_magic(self, dir=None):
        # If any item is empty
        zero_wins = lambda x: x.n_wins() == 0
        some_wins = lambda x: x.n_wins() >  0
        if any(map(zero_wins, self.items)):
            self.items = filter(some_wins, self.items)

            # Ensure we don't have an empty container
            if self.n_items() == 0:
                self.items.append(self.default_item())

            self.fix_cur()
        else:
            # Add another item only if we don't end up with too many
            if self.n_items() + 1 <= type(self).get_max():
                #self.items.append(self.default_item())
                self.items.insert(self.cur + dir.num, self.default_item())

        if self.items == []:
            # Avoid empty containers
            self._item_magic_post_hook()

    def item_magic_next(self): self.item_magic(const.NEXT)
    def item_magic_prev(self): self.item_magic(const.CUR)
