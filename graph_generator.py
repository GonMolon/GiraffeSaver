import sys

import cv2
import networkx as nx

from box import Box
from node import Node


def is_border(im, pixel, height, width, WHITE=255):
    (x, y) = pixel
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            x1 = x + dx
            y1 = y + dy
            if 0 <= x1 < height and 0 <= y1 < width:
                if im[x1, y1] == WHITE:
                    return True
    return False


def fill_color(im, pixel, color, height, width, only_border=False, compute_box=False, WHITE=255):
    total_pixels = 0
    im[pixel] = color
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
                        if (im[x1, y1] != WHITE and im[x1, y1] != color) and \
                                (not only_border or is_border(im, (x1, y1), height, width)):
                            im[x1, y1] = color
                            queue.append((x1, y1))

    if compute_box:
        return box, total_pixels
    else:
        return total_pixels


def generate_graph(img_path):
    img = cv2.imread(img_path, 0)
    ret, im_bw = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)

    height, width = img.shape
    print(height)
    print(width)

    WHITE = 255
    GREY = 128
    GREY_MARKED = 50
    BLACK = 0

    for x in [0, height - 1]:
        for y in range(width):
            if im_bw[x, y] == BLACK:
                fill_color(im_bw, (x, y), WHITE, height, width)
                print("Node filtered")

    for y in [0, width - 1]:
        for x in range(height):
            if im_bw[x, y] == BLACK:
                fill_color(im_bw, (x, y), WHITE, height, width)
                print("Node filtered")

    graph = nx.Graph()
    last_id = 0

    for x in range(height):
        for y in range(width):
            if im_bw[x, y] == BLACK and is_border(im_bw, (x, y), height, width):
                box, outline = fill_color(im_bw, (x, y), GREY, height, width, only_border=True, compute_box=True)
                area = fill_color(im_bw, (x, y), GREY_MARKED, height, width)
                node = Node(last_id, box.get_pos(), outline, area)
                graph.add_node(node)
                print(
                "New node found", node.id, "With area", node.area, "With outline", node.outline, "With pos", node.pos)
                last_id += 1

    for s in graph:
        for t in graph:
            if s.id != t.id:
                graph.add_edge(s, t, weight=s.get_dist(t))

    cv2.imwrite("./output.png", im_bw)
    cv2.imshow("output", im_bw)

    # Wait for quit key
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cv2.destroyAllWindows()