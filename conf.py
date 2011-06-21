import colorsys
import re

import util

class Conf(object):
    "Contains all the config entries"

    ANYTHING = r'.*'
    COMMENT_CHAR = r'#'
    WS = r'\s*'

    HEX_DIGIT    = r'[0-9a-fA-F]'
    HEX_DIGITS_2 = r'%s{%d}' % (HEX_DIGIT, 2)
    HEX_DIGITS_3 = r'%s{%d}' % (HEX_DIGIT, 3)
    HEX_DIGITS_6 = r'%s{%d}' % (HEX_DIGIT, 6)
    HEX_DIGITS_EXTRACT_3 = (r'(%s)' % HEX_DIGIT)    * 3
    HEX_DIGITS_EXTRACT_6 = (r'(%s)' % HEX_DIGITS_2) * 3

    NUM         = r'\d+'
    WS_NUM      = WS + NUM
    COLOR_HEX_3 = r'"#%s"' % HEX_DIGITS_3
    COLOR_HEX_6 = r'"#%s"' % HEX_DIGITS_6
    COLOR_RGB   = r'%s\(%s,%s,%s\)' % (r'rgb', WS_NUM, WS_NUM, WS_NUM)
    COLOR_HSL   = r'%s\(%s,%s,%s\)' % (r'hsl', WS_NUM, WS_NUM, WS_NUM)
    COLOR_HSV   = r'%s\(%s,%s,%s\)' % (r'hsv', WS_NUM, WS_NUM, WS_NUM)
    COLOR_ANY   = r'(?:%s|%s|%s|%s|%s)' % (COLOR_HEX_3, COLOR_HEX_6, COLOR_RGB, COLOR_HSL, COLOR_HSV)

    COLOR_EXTRACT_HEX_3 = r'"#%s"' % HEX_DIGITS_EXTRACT_3
    COLOR_EXTRACT_HEX_6 = r'"#%s"' % HEX_DIGITS_EXTRACT_6
    COLOR_EXTRACT_RGB   = r'%s\((%s),(%s),(%s)\)' % (r'rgb', WS_NUM, WS_NUM, WS_NUM)
    COLOR_EXTRACT_HSL   = r'%s\((%s),(%s),(%s)\)' % (r'hsl', WS_NUM, WS_NUM, WS_NUM)
    COLOR_EXTRACT_HSV   = r'%s\((%s),(%s),(%s)\)' % (r'hsv', WS_NUM, WS_NUM, WS_NUM)

    TRUTHY = r'(?:[Tt]rue|TRUE|[Oo]n|ON|[Yy]es|YES)'
    FALSEY = r'(?:[Ff]alse|FALSE|[Oo]ff|OFF|[Nn]o|NO)'
    BOOL  = r'(?:%s|%s)' % (TRUTHY, FALSEY)
    WORD  = r'\w+'
    IDENT = WORD
    QCHAR = r'(?:[^"]|\\")'
    STR   = QCHAR + r'*'
    INT   = r'[0-9]+'
    SEP_CHAR = r'='

    DEFN = WS + r'(' + IDENT + r')' + WS + SEP_CHAR + WS

    DEFN_PREFIX = WS + r'(' + IDENT + r')' + WS + SEP_CHAR + WS + ANYTHING

    DEFN_STR   = DEFN + r'"(' + STR        + r')"' + WS
    DEFN_WORD  = DEFN + r'('  + WORD       + r')'  + WS
    DEFN_INT   = DEFN + r'('  + INT        + r')'  + WS
    DEFN_BOOL  = DEFN + r'('  + BOOL       + r')'  + WS
    DEFN_COLOR = DEFN + r'('  + COLOR_ANY  + r')'  + WS

    COMMENT   = WS + COMMENT_CHAR + ANYTHING

    def __init__(self):
        "Search for user config files and load them"
        self.set_defaults()
        self.load("cakewm.conf")

    def set_defaults(self):
        self.stuff = Conf.attr_to_default_val.copy()

    def load(self, file):
        util.debug("loading config: %s" % file)
        with open(file) as f:
            for lineno, line in enumerate(f.readlines(), start=1):
                line = line.rstrip("\n")
                self.process_line(lineno, line)

    def __getattr__(self, attr):
        return self.stuff[attr]

    def parse_str(str):
        # Remove quotes
        str = str[1:-1]
        # Replace escaped quotes with real ones
        str = str.replace(r'\"', r'"')
        return str

    def parse_color_any(color):
        for regex, parse_func in Conf.color_regex_to_parse_func.iteritems():
            if re.match(regex, color):
                return parse_func(color)

        util.error("Could not parse color: %s" % color)

    def parse_color_hex_3(hex):
        r, g, b = re.findall(Conf.COLOR_EXTRACT_HEX_3, hex)[0]
        # Remember that #F03 means #FF0033, so duplicated digits
        r = int(r + r, 16)
        g = int(g + g, 16)
        b = int(b + b, 16)
        util.rgb_assert((r, g, b))

        return (r, g, b)

    def parse_color_hex_6(hex):
        r, g, b = re.findall(Conf.COLOR_EXTRACT_HEX_6, hex)[0]
        r = int(r, 16)
        g = int(g, 16)
        b = int(b, 16)
        util.rgb_assert((r, g, b))

        return (r, g, b)

    def parse_color_rgb(rgb):
        r, g, b = re.findall(Conf.COLOR_EXTRACT_RGB, rgb)[0]
        r = int(r)
        g = int(g)
        b = int(b)
        util.rgb_assert((r, g, b))

        return (r, g, b)

    def parse_color_hsl(hsl):
        h, s, l = re.findall(Conf.COLOR_EXTRACT_HSL, hsl)[0]
        h = int(h) / 360.0
        s = int(s) / 100.0
        l = int(l) / 100.0
        util.hsl_assert((h, s, l))
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        r = int(round(255 * r))
        g = int(round(255 * g))
        b = int(round(255 * b))
        util.rgb_assert((r, g, b))

        return (r, g, b)

    def parse_color_hsv(hsv):
        h, s, v = re.findall(Conf.COLOR_EXTRACT_HSV, hsv)[0]
        h = int(h) / 360.0
        s = int(s) / 100.0
        v = int(v) / 100.0
        util.hsv_assert((h, s, v))
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        r = int(round(255 * r))
        g = int(round(255 * g))
        b = int(round(255 * b))
        util.rgb_assert((r, g, b))

        return (r, g, b)

    def parse_bool(bool):
        if   re.match(Conf.TRUTHY, bool): return True
        elif re.match(Conf.FALSEY, bool): return False
        else:
            util.errors(
                "invalid boolean constant: %s; " % bool,
                "expecting true/false, yes/no, on/off"
            )

    def process_defn_line(self, lineno, line):
        attr  = re.findall(Conf.DEFN_PREFIX, line)[0]
        type  = Conf.attr_to_type [attr]
        func  = Conf.type_to_func [type]
        regex = Conf.type_to_regex[type]
        if re.match(regex, line):
            attr, val = re.findall(regex, line)[0]
            self.stuff[attr] = func(val)
        else:
            util.error("could not parse line %i: %s" % (lineno, line))

    def process_line(self, lineno, line):
        if   re.match(Conf.DEFN_PREFIX, line): self.process_defn_line(lineno, line)
        elif re.match(Conf.COMMENT,     line): pass
        elif re.match(Conf.SPACE,       line): pass
        else:
            util.error("could not parse line %i: %s" % (lineno, line))

    def __repr__(self):
        title = "[Conf]"
        pairs = self.stuff.items()
        pairs.sort()
        func  = lambda pair: "------- %s = %s" % pair
        defns = map(func, pairs)
        return title + "\n" + "\n".join(defns)

    type_to_func = {
        "int":   int,
        "str":   parse_str,
        "word":  lambda x: x,
        "bool":  parse_bool,
        "color": parse_color_any,
    }

    type_to_regex = {
        "int":   DEFN_INT,
        "str":   DEFN_STR,
        "word":  DEFN_WORD,
        "bool":  DEFN_BOOL,
        "color": DEFN_COLOR,
    }

    attr_to_type = {
        "max_stacks":      "int",
        "max_columns":     "int",
        "exit_message":    "bool",
        "welcome_message": "bool",
        "test_color":      "color",
    }

    attr_to_default_val = {
        "max_stacks":      9,
        "max_columns":     9,
        "exit_message":    False,
        "welcome_message": False,
        "test_color":      (123, 4, 89),
    }

    color_regex_to_parse_func = {
        COLOR_HEX_3: parse_color_hex_3,
        COLOR_HEX_6: parse_color_hex_6,
        COLOR_RGB:   parse_color_rgb,
        COLOR_HSL:   parse_color_hsl,
        COLOR_HSV:   parse_color_hsv,
    }

    parse_bool = staticmethod(parse_bool)
    parse_str  = staticmethod(parse_str)

conf = Conf()
