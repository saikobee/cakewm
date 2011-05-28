class Ratio(object):
    "Ratio merely has one member: `ratio', with a default value: 0.50"
    DEFAULT = 0.50
    MIN     = 0.05
    MAX     = 1 - MIN
    INC     = 0.05
    DEC     = -INC

    def __init__(self, ratio=DEFAULT):
        self.ratio = ratio

    def complement_ratio(self): self.ratio = 1 - self.ratio
    def inc_ratio(self): self.mod_ratio(Ratio.INC)
    def dec_ratio(self): self.mod_ratio(Ratio.DEC)
    def mod_ratio(self, number):
        self.ratio = util.clamp(self.ratio + number, Ratio.MIN, Ratio.MAX)
