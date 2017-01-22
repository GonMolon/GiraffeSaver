from Queue import PriorityQueue

import node
from utils import RatioEvaluator

act_level = 0
max_level = -1


def compare_nodes(evaluator, g1, g2, from1, from2, nodes1, nodes2, available1, available2):
    global act_level
    global max_level
    nodes1 = filter(lambda n: n not in available1, nodes1)
    nodes2 = filter(lambda n: n not in available2, nodes2)
    if len(nodes1) == 0:
        nodes1 = list(available1)
    if len(nodes2) == 0:
        nodes2 = list(available2)
    for n1 in nodes1:
        if n1 not in available1:
            pass
        candidate = False
        for n2 in nodes2:
            if n2 not in available2:
                pass
            if evaluator.add_nodes(from1, from2, n1, n2):
                candidate = True
                available1.remove(n1)
                available2.remove(n2)
                act_level += 1
                if act_level > max_level:
                    max_level = act_level
                aux1 = list(g1.edges(n1))
                aux2 = list(g2.edges(n2))
                compare_nodes(evaluator, g1, g2, aux1, aux2, available1, available2)
                available1.put(n1)
                available2.put(n2)
                evaluator.rollback()
                act_level -= 1
        if not candidate:
            available1.remove(n1)
            aux1 = list(available1)
            aux2 = list(available2)
            compare_nodes(evaluator, g1, g2, aux1, nodes2, available1, available2)
            nodes1.append(n1)


def compare_graphs(graph1, graph2):
    nodes1 = list(graph1.nodes())
    nodes2 = list(graph2.nodes())

    max = min(len(nodes1), len(nodes2))

    compare_nodes(RatioEvaluator(), graph1, graph2, nodes1, nodes2, set(nodes1), set(nodes2))

    print(max_level / float(max))
