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

    def get_ratio(self, other):
        ratios = [self.area/float(other.area), self.outline/float(other.outline)]
        mean_ratio = Node.__mean(ratios)
        variance_ratio = Node.__variance(mean_ratio, ratios)
        return mean_ratio, variance_ratio

    @staticmethod
    def __mean(list):
        return sum(list)/len(list)

    @staticmethod
    def __variance(mean, list):
        aux = [math.pow(x-mean, 2) for x in list]
        return sum(aux)/len(aux)

