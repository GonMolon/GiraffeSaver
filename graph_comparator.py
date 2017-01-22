import node


def compare_graphs(graph1, graph2):
    nodes1 = list(graph1.nodes())
    nodes2 = list(graph2.nodes())

    for n1 in nodes1:
        for n2 in nodes2:
            ratio, variance = n1.get_ratio(n2)
            if variance < 0.5:
                print(ratio)
