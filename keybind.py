import pygame
import pygame.locals

import pypixel

import util
import const

class Keybind(object):
    def __init__(self, key_str):
        self.orig_str = key_str
        self.modifiers, self.key = Keybind.parse_key_str(key_str)

    @staticmethod
    def parse_key_str(key_str):
        mods, key = key_str.split('-')

        mods = map(lambda mod: Keybind.mods[mod], mods.upper())
        mod  = reduce(lambda sum, mod: sum | mod, mods)
        key  = Keybind.keys[key.lower()]

        return (mod, key)

    def __hash__(self):
        return hash(self.as_tuple())

    def __eq__(self, other):
        if isinstance(other, tuple): return self.as_tuple() == other
        else:                        return self.as_tuple() == other.as_tuple()

    def as_tuple(self):
        return (self.modifiers, self.key)

    def __str__(self):
        return "<%s>" % self.orig_str

    mods = {
        "W": const.KMOD_SUPER,
        "S": const.KMOD_SHIFT,
        "C": const.KMOD_CTRL,
        "A": const.KMOD_ALT,
    }

    alpha   = map(chr, range(ord('a'), ord('z') + 1))
    numbers = map(str, range(10))

    keys = {}
    keys.update(dict(((letter, getattr(pygame.locals, "K_" + letter)) for letter in alpha)))
    keys.update(dict(((number, getattr(pygame.locals, "K_" + number)) for number in numbers)))
    keys.update(util.invert_dict({
        pygame.locals.K_BACKSPACE    : ["backspace"],
        pygame.locals.K_TAB          : ["tab"],
        pygame.locals.K_RETURN       : ["return", "enter"],
        pygame.locals.K_ESCAPE       : ["escape", "esc"],
        pygame.locals.K_SPACE        : ["space"],
        pygame.locals.K_EXCLAIM      : ["!"],
        pygame.locals.K_QUOTEDBL     : ["\""],
        pygame.locals.K_HASH         : ["#"],
        pygame.locals.K_DOLLAR       : ["$"],
        pygame.locals.K_AMPERSAND    : ["&"],
        pygame.locals.K_QUOTE        : ["'"],
        pygame.locals.K_LEFTPAREN    : ["("],
        pygame.locals.K_RIGHTPAREN   : [")"],
        pygame.locals.K_ASTERISK     : ["*"],
        pygame.locals.K_PLUS         : ["+"],
        pygame.locals.K_COMMA        : [","],
        pygame.locals.K_MINUS        : ["minus", "-"],
        pygame.locals.K_PERIOD       : ["."],
        pygame.locals.K_SLASH        : ["/"],
        pygame.locals.K_COLON        : [":"],
        pygame.locals.K_SEMICOLON    : [";"],
        pygame.locals.K_LESS         : ["less", "lt", "<"],
        pygame.locals.K_EQUALS       : ["="],
        pygame.locals.K_GREATER      : ["greater", "gt", ">"],
        pygame.locals.K_QUESTION     : ["?"],
        pygame.locals.K_AT           : ["@"],
        pygame.locals.K_LEFTBRACKET  : ["["],
        pygame.locals.K_BACKSLASH    : ["\\"],
        pygame.locals.K_RIGHTBRACKET : ["]"],
        pygame.locals.K_CARET        : ["^"],
        pygame.locals.K_UNDERSCORE   : ["_"],
        pygame.locals.K_BACKQUOTE    : ["`"],
    }))
