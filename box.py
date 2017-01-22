class Box:
    def __init__(self):
        self.minX = None
        self.minY = None
        self.maxX = None
        self.maxY = None
        self.init = False

    def add_point(self, pixel):
        x, y = pixel
        if not self.init:
            self.init = True
            self.minX = self.maxX = x
            self.minY = self.maxY = y
        else:
            if x < self.minX:
                self.minX = x
            if y < self.minY:
                self.minY = y
            if self.maxX < x:
                self.maxX = x
            if self.maxY < y:
                self.maxY = y

    def get_pos(self):
        return (self.maxX + self.minX) / 2, (self.maxY + self.minY) / 2
