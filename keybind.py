import pygame
import pygame.locals

import pypixel

import util

class Keybind(object):
    def __init__(self, key_str):
        self.modifiers, self.key = Keybind.parse_key_str(key_str)

    @staticmethod
    def parse_key_str(key_str):
        mod, key = key_str.split('-')

        mod = Keybind.mods[mod.upper()]
        key = Keybind.keys[key.lower()]

        return (mod, key)

    mods = {
        "W": pygame.locals.KMOD_META,
        "S": pygame.locals.KMOD_SHIFT,
        "C": pygame.locals.KMOD_CTRL,
        "A": pygame.locals.KMOD_ALT,
    }
