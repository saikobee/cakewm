import util
from   util import conf

class Magic(object):
    '''The subclass must define MAX as a class variable and
    default_item() as an instance method'''

    def item_magic(self):
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
                self.items.append(self.default_item())
