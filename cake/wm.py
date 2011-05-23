class WM(object):
    def __init__(self, display):
        self.display = display

    def set_focii(self):
        for i_screen, screen in enumerate(self.display.screens):
            for i_tag, tag in enumerate(screen.tags):
                for i_col, col in enumerate(tag.cols):
                    for i_stack, stack in enumerate(col.stacks):
                        stack.unfocus()

                        indices = (
                            i_screen,
                            i_tag,
                            i_col,
                            i_stack,
                        )

                        curs = (
                            self.display.cur,
                            screen.cur,
                            tag.cur,
                            col.cur,
                        )

                        if indices == curs:
                            stack.focus()

    def draw(self):
        for i_screen, screen in enumerate(self.display.screens):
            for i_tag, tag in enumerate(screen.tags):
                for i_col, col in enumerate(tag.cols):
                    for i_stack, stack in enumerate(col.stacks):
                        indices = (
                            i_screen,
                            i_tag,
                        )

                        curs = (
                            self.display.cur,
                            screen.cur,
                        )

                        if indices == curs:
                            stack.draw()

    def organize(self):
        for screen in self.display.screens:
            for tag in screen.tags:
                tag.organize(screen) 
