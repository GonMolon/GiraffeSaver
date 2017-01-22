import time

from utils import RatioEvaluator


act_level = 0
max_level = -1

nodes1 = nodes2 = None
g1 = g2 = None
available1 = available2 = None
evaluator = None

timeout = None


def compare_nodes(act1, act2):
    if time.time() > timeout:
        return

    global act_level
    global max_level

    if len(available1) == 0 or len(available2) == 0:
        return

    for n1 in act1:
        if n1 not in available1:
            continue
        candidate = False
        for n2 in act2:
            if n2 not in available2:
                continue
            if evaluator.add_nodes(n1, n2):
                candidate = True
                available1.remove(n1)
                available2.remove(n2)
                act_level += 1
                if act_level > max_level:
                    max_level = act_level
                compare_nodes(set(g1.neighbors(n1)), set(g2.neighbors(n2)))
                available1.add(n1)
                available2.add(n2)
                act_level -= 1
            evaluator.rollback()
        if not candidate:
            available1.remove(n1)
            compare_nodes(set(available1), set(available2))
            available1.add(n1)


def compare_graphs(graph1, graph2):
    global evaluator, nodes1, nodes2, g1, g2
    nodes1 = list(graph1.nodes())
    nodes2 = list(graph2.nodes())[::-1]
    max = min(len(nodes1), len(nodes2))

    evaluator = RatioEvaluator()

    g1 = graph1
    g2 = graph2

    global available1, available2
    available1 = set(nodes1)
    available2 = set(nodes2)

    global timeout
    timeout = time.time() + 4
    compare_nodes(set(nodes1), set(nodes2))

    return max_level / float(max)
