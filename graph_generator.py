import cv2
import networkx as nx

from box import Box
from node import Node


WHITE = 255
GREY = 128
GREY_MARKED = 50
BLACK = 0


def is_border(pixel):
    (x, y) = pixel
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            x1 = x + dx
            y1 = y + dy
            if 0 <= x1 < height and 0 <= y1 < width:
                if img[x1, y1] == WHITE:
                    return True
    return False


def fill_color(pixel, color, only_border=False, compute_box=False):
    total_pixels = 0
    img[pixel] = color
    queue = [pixel]
    box = Box()

    while queue:
        (x, y) = queue[0]
        queue.pop(0)
        total_pixels += 1
        if compute_box:
            box.add_point((x, y))
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (dx != 0 or dy != 0) and (dx == 0 or dy == 0):
                    x1 = x + dx
                    y1 = y + dy
                    if 0 <= x1 < height and 0 <= y1 < width:
                        if (img[x1, y1] != WHITE and img[x1, y1] != color) and \
                                (not only_border or is_border((x1, y1))):
                            img[x1, y1] = color
                            queue.append((x1, y1))

    if compute_box:
        return box, total_pixels
    else:
        return total_pixels


def filter_nodes():
    for x in [0, height - 1]:
        for y in range(width):
            if img[x, y] == BLACK:
                fill_color((x, y), WHITE)
                print("Node filtered")

    for y in [0, width - 1]:
        for x in range(height):
            if img[x, y] == BLACK:
                fill_color((x, y), WHITE)
                print("Node filtered")


def add_nodes(graph):
    last_id = 0

    for x in range(height):
        for y in range(width):
            if img[x, y] == BLACK and is_border((x, y)):
                box, outline = fill_color((x, y), GREY, only_border=True, compute_box=True)
                area = fill_color((x, y), GREY_MARKED)
                node = Node(last_id, box.get_pos(), outline, area)
                graph.add_node(node)
                print(
                    "New node found", node.id, "With area", node.area, "With outline", node.outline, "With pos",
                    node.pos)
                last_id += 1


def add_edges(graph):
    for s in graph:
        for t in graph:
            if s.id != t.id:
                graph.add_edge(s, t, weight=s.get_dist(t))

img = None
height = width = None


def generate_graph(img_path):
    global img, height, width
    img = cv2.imread(img_path, 0)
    ret, img = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
    height, width = img.shape

    filter_nodes()

    graph = nx.Graph()

    add_nodes(graph)
    add_edges(graph)

    return graph
