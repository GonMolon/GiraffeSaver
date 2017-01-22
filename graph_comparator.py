from Queue import PriorityQueue

import node
from utils import RatioEvaluator

act_level = 0
max_level = -1

nodes1 = nodes2 = None
available1 = available2 = None
evaluator = None


def compare_nodes():
    global act_level
    global max_level

    if len(available1) == 0 or len(available2) == 0:
        return

    print("------------------------------------------------------------------------------------------------------------------------------")
    print(filter(lambda n: n in available1, nodes1))
    print(filter(lambda n: n in available2, nodes2))
    print("------------------------------------------------------------------------------------------------------------------------------")

    for n1 in nodes1:
        if n1 not in available1:
            continue
        candidate = False
        for n2 in nodes2:
            if n2 not in available2:
                continue
            if evaluator.add_nodes(n1, n2):
                candidate = True
                available1.remove(n1)
                available2.remove(n2)
                act_level += 1
                if act_level > max_level:
                    max_level = act_level
                compare_nodes()
                available1.add(n1)
                available2.add(n2)
                act_level -= 1
            evaluator.rollback()
        if not candidate:
            available1.remove(n1)
            compare_nodes()
            available1.add(n1)


def compare_graphs(graph1, graph2):
    global evaluator, nodes1, nodes2, available1, available2
    nodes1 = list(graph1.nodes())
    nodes2 = list(graph2.nodes())[::-1]
    max = min(len(nodes1), len(nodes2))

    evaluator = RatioEvaluator()

    available1 = set(nodes1)
    available2 = set(nodes2)

    compare_nodes()

    print(max_level / float(max))
