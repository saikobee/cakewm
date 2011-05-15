class WM(object):
    def __init__(self, display):
        self.display = display

    def organize(self):
        # Only support one screen in the pypixel backend...
        i_screen = 0
        screen   = self.display.screens[i_screen]

        for i_tag, tag in enumerate(screen.tags):
            for i_col, col in enumerate(tag.cols):
                for i_stack, stack in enumerate(col.stacks):
                    for i_win, win in enumerate(stack.windows):
                        win.unfocus()

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
                            # stack.cur,
                        )

                        if indices == curs:
                            win.focus()

                        win.w = screen.w / len(tag.cols)
                        win.h = screen.h / len(col.stacks)

                        win.x = win.w * i_col
                        win.y = win.h * i_stack

                    stack.draw()
