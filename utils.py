import math


class RatioEvaluator:
    def __init__(self):
        self.ratios = []
        self.total = 0.0
        self.var = None

    def mean(self):
        if len(self.ratios) == 0:
            return 0
        return self.total / len(self.ratios)

    def variance(self):
        mean = self.mean()
        aux = [math.pow(x - mean, 2) for x in self.ratios]
        return sum(aux) / len(aux)

    def add_nodes(self, n1, n2):
        node_ratios = n1.get_ratios(n2)
        self.total += sum(node_ratios)
        self.ratios += node_ratios
        self.var = self.variance()
        return self.var < 0.1

    def rollback(self):
        remove = self.ratios[-2:]
        self.total -= sum(remove)
        del self.ratios[-2:]
        if len(self.ratios) != 0:
            self.var = self.variance()
        else:
            self.total = 0.0
            self.var = None
