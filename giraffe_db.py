import io
import pickle
import sys
from os import listdir
from os.path import isfile, join

from graph_comparator import compare_graphs
from graph_generator import generate_graph


def store_giraffe(path, name):
    graph = generate_graph(path)
    f = io.open("db/" + name, 'wb')
    pickle.dump(graph, f)
    f.close()


def search_giraffe(path):
    root_path = "./db"
    files = [open(join(root_path, f), 'rb') for f in listdir(root_path) if isfile(join(root_path, f))]
    graph_list = [pickle.load(file) for file in files]
    for file in files:
        file.close()
    compare_graphs(graph_list[0], graph_list[0])


def main():
    search_giraffe(sys.argv[1])


if __name__ == "__main__":
    main()