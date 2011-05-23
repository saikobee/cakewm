class Ratio(object):
    "Ratio merely has one member: `ratio', with a default value: 0.50"
    DEFAULT = 0.50
    MIN     = 0.10
    MAX     = 0.90

    def __init__(self, ratio=DEFAULT):
        self.ratio = ratio
