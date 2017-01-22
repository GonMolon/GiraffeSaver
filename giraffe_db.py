import sys

from graph_generator import generate_graph


def store_giraffe(path):
    graph = generate_graph(path)


def search_giraffe(path):
    graph = generate_graph(path)


def main():
    store_giraffe(sys.argv[1])


if __name__ == "__main__":
    main()
