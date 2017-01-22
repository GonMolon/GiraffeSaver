import node
from utils import RatioEvaluator


def compare_graphs(graph1, graph2):
    nodes1 = list(graph1.nodes())
    nodes2 = list(graph2.nodes())

    for n1 in nodes1:
        ratios = RatioEvaluator()
        for n2 in nodes2:
            if not ratios.add_nodes(n1, n2):
                break
            else:
                print(ratios.var)
