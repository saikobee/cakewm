import re

import util

class Conf(object):
    "Contains all the config entries"

    ANYTHING = r'.*'
    COMMENT_CHAR = r'#'
    WS = r'\s*'

    TRUTHY = r'(?:[Tt]rue|TRUE|[Oo]n|ON|[Yy]es|YES)'
    FALSEY = r'(?:[Ff]alse|FALSE|[Oo]ff|OFF|[Nn]o|NO)'
    BOOL  = r'(?:' + TRUTHY + r'|' + FALSEY + r')'
    WORD  = r'\w+'
    IDENT = WORD
    QCHAR = r'(?:[^"]|\\")'
    STR   = QCHAR + r'*'
    INT   = r'[0-9]+'
    SEP_CHAR = r'='

    DEFN = WS + r'(' + IDENT + r')' + WS + SEP_CHAR + WS

    DEFN_PREFIX = WS + r'(' + IDENT + r')' + WS + SEP_CHAR + WS + ANYTHING

    DEFN_STR  = DEFN + r'"(' + STR  + r')"' + WS
    DEFN_WORD = DEFN + r'('  + WORD + r')'  + WS
    DEFN_INT  = DEFN + r'('  + INT  + r')'  + WS
    DEFN_BOOL = DEFN + r'('  + BOOL + r')'  + WS

    COMMENT   = WS + COMMENT_CHAR + ANYTHING

    TRUTHY      = re.compile(TRUTHY)
    FALSEY      = re.compile(FALSEY)
    DEFN_STR    = re.compile(DEFN_STR)
    DEFN_WORD   = re.compile(DEFN_WORD)
    DEFN_INT    = re.compile(DEFN_INT)
    DEFN_BOOL   = re.compile(DEFN_BOOL)
    COMMENT     = re.compile(COMMENT)
    DEFN_PREFIX = re.compile(DEFN_PREFIX)

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

    def parse_bool(bool):
        if   Conf.TRUTHY.match(bool): return True
        elif Conf.FALSEY.match(bool): return False
        else:
            msg = (
                "invalid boolean constant: %s; " +
                "expecting true/false, yes/no, on/off"
            ) % bool
            util.error(msg)

    def process_defn_line(self, lineno, line):
        attr  = Conf.DEFN_PREFIX.findall(line)[0]
        type  = Conf.attr_to_type [attr]
        func  = Conf.type_to_func [type]
        regex = Conf.type_to_regex[type]
        if regex.match(line):
            attr, val = regex.findall(line)[0]
            self.stuff[attr] = func(val)
        else:
            util.error("could not parse line %i: %s" % (lineno, line))

    def process_line(self, lineno, line):
        if   Conf.DEFN_PREFIX.match(line): self.process_defn_line(lineno, line)
        elif Conf.COMMENT    .match(line): pass
        elif Conf.SPACE      .match(line): pass
        else:
            util.error("could not parse line %i: %s" % (lineno, line))

    def __repr__(self):
        title = "[Conf]"
        pairs = self.stuff.items()
        func  = lambda pair: "--- %s = %s" % pair
        defns = map(func, pairs)
        return title + "\n" + "\n".join(defns)

    type_to_func = {
        "int":  int,
        "str":  parse_str,
        "word": lambda x: x,
        "bool": parse_bool,
    }

    type_to_regex = {
        "int":  DEFN_INT,
        "str":  DEFN_STR,
        "word": DEFN_WORD,
        "bool": DEFN_BOOL,
    }

    attr_to_type = {
        "max_stacks":   "int",
        "max_columns":  "int",
        "exit_message": "bool",
        "welcome_message": "bool",
    }

    attr_to_default_val = {
        "max_stacks":   9,
        "max_columns":  9,
        "exit_message": False,
        "welcome_message": False,
    }

    parse_bool = staticmethod(parse_bool)
    parse_str  = staticmethod(parse_str)

conf = Conf()
