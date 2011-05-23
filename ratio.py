class Ratio(object):
    "Ratio merely has one member: `ratio', with a default value: 0.50"
    DEFAULT = 0.50
    MIN     = 0.05
    MAX     = 1 - MIN

    def __init__(self, ratio=DEFAULT):
        self.ratio = ratio
