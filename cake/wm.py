class WM(object):
    def __init__(self, display):
        self.display = display

    def organize(self):
        for i_screen, screen in enumerate(self.display.screens):
            n_screens = len(self.display.screens)

            for i_tag, tag in enumerate(screen.tags):
                n_tags = len(screen.tags)

                for i_col, col in enumerate(tag.cols):
                    n_cols = len(tag.cols)

                    for i_stack, stack in enumerate(col.stacks):
                        n_stacks = len(col.stacks)

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

                        stack.w = screen.w / n_cols
                        stack.h = screen.h / n_stacks
                        stack.x = stack.w * i_col
                        stack.y = stack.h * i_stack

                        # We might not use every pixel on the screen
                        # given this approach, so fix the things near
                        # screen edges.

                        # Right edge
                        if i_col == n_cols - 1:
                            stack.w = screen.w - (int(screen.w / n_cols) * (n_cols - 1))

                        # Bottom edge
                        if i_stack == n_stacks - 1:
                            stack.h = screen.h - (int(screen.h / n_stacks) * (n_stacks - 1))

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
