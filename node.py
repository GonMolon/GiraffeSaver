import math


class Node:
    def __init__(self, id, pos, outline, area):
        self.id = id
        self.pos = pos
        self.outline = outline
        self.area = area

    def get_dist(self, other):
        x1, y1 = self.pos
        x2, y2 = other.pos
        return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))