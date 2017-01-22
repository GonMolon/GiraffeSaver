import io
import pickle
import sys
from os import listdir
from os.path import isfile, join

from graph_comparator import compare_graphs
from graph_generator import generate_graph


def store_giraffe(path, name):
    graph = generate_graph(path)
    graph.name = name
    f = io.open("db/" + name, 'wb')
    pickle.dump(graph, f)
    f.close()


def search_giraffe(path):
    root_path = "./db"
    files = [open(join(root_path, f), 'rb') for f in listdir(root_path) if isfile(join(root_path, f))]
    graph_list = [pickle.load(file) for file in files]
    for file in files:
        file.close()
    graph = generate_graph(path)
    for g in graph_list:
        print("Similarity with " + g.name, compare_graphs(graph, g))

def main():
    path = sys.argv[1]
    if len(sys.argv) > 2:
        name = sys.argv[2]
        store_giraffe(path, name)
    else:
        search_giraffe(path)

if __name__ == "__main__":
    main()
