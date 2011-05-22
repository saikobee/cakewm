class Ratio(object):
    "Ratio merely has one member: `ratio', with a default value: 0.50"
    DEFAULT_RATIO = 0.50

    def __init__(self, ratio=DEFAULT_RATIO):
        self.ratio = ratio
