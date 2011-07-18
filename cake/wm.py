import pypixel

import util

from conf import conf

class WM(object):
    def __init__(self, **kwargs):
        self.display = kwargs["display"]
        self.bar_top = ""
        self.bar_bot = ""

    def set_resolution(self, res):
        self.display.set_resolution(res)
        self.organize()

    def draw_wallpaper(self):
        grey0 = (32, ) * 3
        grey1 = (128,) * 3

        screen = self.display.item()
        w, h   = screen.dim
        for x in xrange(0, w, 2):
            p0 = (x, 0    )
            p1 = (x, h - 1)
            pypixel.line(grey0, p0, p1)

            p0 = (x + 1, 0    )
            p1 = (x + 1, h - 1)
            pypixel.line(grey1, p0, p1)

    def debug_bars(self):
        util.clear()
        util.echo("TOP:", self.bar_top)
        util.echo("BOT:", self.bar_bot)

    def update_bars(self, mgs=""):
        self.update_top_bar(msg)
        self.update_bottom_bar()

    def update_top_bar(self, msg=""):
        self.top_bar = msg

    def update_bottom_bar(self):
        d = self.display
        try:
            self.bar_bot = "%s <RALIGN> screen:[%d/%d] tag:[%d/%d] window:[%02d/%02d]" % (
                d.cur_win_title() or "",

                d.cur_screen() + 1,
                d.tot_screens(),

                d.cur_tag() + 1,
                d.tot_tags(),

                d.cur_win() + 1,
                d.tot_wins(),
            )
        except Exception as e:
            util.debugs("issue updating bottom bar", str(e))

    def draw_bars(self):
        screen = self.display.item()
        tag    = screen.item()

        if tag.bar_hidden:
            return

        color     = conf.bar_color
        highlight = conf.bar_highlight
        bh        = conf.bar_height

        # Top bar
        x, y = 0, 0
        w, h = screen.dim
        rect = ((x, y),      (w,     bh))     # (x, y), (w, h)
        line = ((x, y - 2 + bh), (w - 1, y - 2 + bh)) # (x, y), (x, y)

        pypixel.rectangle(color, rect)
        pypixel.line(highlight, *line)

        # Top bar
        x, y = screen.dim
        x, y = 0, y - bh
        w, h = screen.dim
        w, h = w, bh
        rect = ((x, y),     (w,     bh))    # (x, y), (w, h)
        line = ((x, y + 1), (w - 1, y + 1)) # (x, y), (x, y)

        pypixel.rectangle(color, rect)
        pypixel.line(highlight, *line)

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
                indices = (
                    i_screen,
                    i_tag,
                )

                curs = (
                    self.display.cur,
                    screen.cur,
                )

                # Be nice and let the user see their desktop
                if tag.n_stacks() <= 1 and tag.n_wins() == 0:
                    return

                if tag.fullscreen and indices == curs:
                    tag.draw_fullscreen(screen)
                    return
                n_cols = len(tag.cols)
                for i_col, col in enumerate(tag.cols):
                    n_stacks = len(col.stacks)
                    for i_stack, stack in enumerate(col.stacks):

                        indices = (
                            i_screen,
                            i_tag,
                        )

                        curs = (
                            self.display.cur,
                            screen.cur,
                        )

                        hint = ""
                        if i_col   != (n_cols   - 1): hint += "r"
                        if i_col   != 0             : hint += "l"
                        if i_stack != (n_stacks - 1): hint += "b"
                        if i_stack != 0             : hint += "t"

                        if indices == curs:
                            stack.draw(hint=hint)

    def organize(self):
        for screen in self.display.screens:
            for tag in screen.tags:
                tag.organize(screen)
