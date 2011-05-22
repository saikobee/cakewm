class FloatingRect(object):
    def __init__(self, **kwargs):
        self.rect = kwargs.get("rect", ((0, 0), (0, 0)))

        self.size = kwargs.get("size", (0, 0))
        self.pos  = kwargs.get("pos",  (0, 0))

        self.x = kwargs.get("x", 0)
        self.y = kwargs.get("y", 0)

        self.w = kwargs.get("w", 20)
        self.h = kwargs.get("h", 20)

    @property
    def size(self):
        return (self.w, self.h)

    @size.setter
    def size(self, size):
        self.w, self.h = size

    @property
    def pos(self):
        return (self.x, self.y)

    @pos.setter
    def pos(self, pos):
        self.x, self.y = pos

    @property
    def rect(self):
        return (self.pos, self.size)

    @rect.setter
    def rect(self, rect):
        self.pos, self.size = rect
