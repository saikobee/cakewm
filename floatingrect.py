class FloatingRect(object):
    def __initialize__(self, **kwargs):
        self.rect = kwargs.get("rect", ((0, 0), (0, 0)))

        self.size = kwargs.get("size", (0, 0))
        self.pos  = kwargs.get("pos",  (0, 0))

        self.x = kwargs.get("x", 0)
        self.y = kwargs.get("y", 0)

        self.w = kwargs.get("w", 20)
        self.h = kwargs.get("h", 20)
