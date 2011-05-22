class WM(object):
    def __init__(self, display):
        self.display = display

    def organize(self):
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

                        stack.w = screen.w / len(tag.cols)
                        stack.h = screen.h / len(col.stacks)
                        stack.x = stack.w * i_col
                        stack.y = stack.h * i_stack

                        stack.organize()

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
