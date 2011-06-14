import re

import util

class ParseError(Exception): pass

class Conf(object):
    "Contains all the config entries"

    ANYTHING = r'.*'
    COMMENT_CHAR = r'#'
    WS = r'\s*'

    BOOL  = r'(?:(?i)true|false|on|off|yes|no)'
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
        with open(file) as f:
            for line in f.readlines():
                self.process_line(line)

    def __getattr__(self, attr):
        return self.stuff[attr]

    @staticmethod
    def parse_str(str):
        # Remove quotes
        str = str[1:-1]
        # Replace escaped quotes with real ones
        str = str.replace(r'\"', r'"')
        return str

    @staticmethod
    def parse_bool(bool):
        if bool.lower() in ("true", "yes", "on"):
            return True
        elif bool.ower() in ("false", "no", "off"):
            return False
        else:
            msg = (
                "Invalid boolean constant: %s; " +
                "expecting true/false, yes/no, on/off"
            ) % bool
            return ParseError(msg)

    def process_defn_line(self, line):
        attr  = Conf.DEFN_PREFIX.findall(line)[0]
        type  = Conf.attr_to_type [attr]
        func  = Conf.type_to_func [type]
        regex = Conf.type_to_regex[type]
        if regex.match(line):
            attr, val = regex.findall(line)[0]
            self.stuff[attr] = func(val)
        else:
            raise ParseError("Error parsing line: %s" % line)

    def process_line(self, line):
        if   Conf.DEFN_PREFIX.match(line): self.process_defn_line(line)
        elif Conf.COMMENT    .match(line): pass
        elif Conf.SPACE      .match(line): pass
        else:
            raise ParseError("Bad input line: " + line)

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
    }

    attr_to_default_val = {
        "max_stacks":   9,
        "max_columns":  9,
    }
