class Focusable(object):
    def __init__(self):
        self.focused = False

    def   focus(self): self.focused = True
    def unfocus(self): self.focused = False

    def focus_toggle(self):
        if self.focused: self.unfocus()
        else:            self.  focus()
