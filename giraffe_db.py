import sys
import pickle
import io
from os import listdir
from os.path import isfile, join

from graph_generator import generate_graph

def store_giraffe(path):
    graph = generate_graph(path)
    f = io.open(path, 'rb')
    pickle.dump(graph, f)
    f.close()


def search_giraffe(path):
    onlyfiles = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
    print onlyfiles
    graph_list = [generate_graph(file) for file in onlyfiles]
    return graph_list

def main():

    store_giraffe(sys.argv[1])


if __name__ == "__main__":
    main()
