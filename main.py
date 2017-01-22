import cv2
import sys
import networkx as nx
import math


class Node:
    def __init__(self, id, pos, outline, area):
        self.id = id
        self.pos = pos
        self.outline = outline
        self.area = area

    def get_dist(self, other):
        x1, y1 = self.pos
        x2, y2 = other.pos
        return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))


class Box:
    def __init__(self):
        self.minX = None
        self.minY = None
        self.maxX = None
        self.maxY = None
        self.init = False

    def add_point(self, pixel):
        x, y = pixel
        if not self.init:
            self.init = True
            self.minX = self.maxX = x
            self.minY = self.maxY = y
        else:
            if x < self.minX:
                self.minX = x
            if y < self.minY:
                self.minY = y
            if self.maxX < x:
                self.maxX = x
            if self.maxY < y:
                self.maxY = y

    def get_pos(self):
        return (self.maxY + self.minX) / 2, (self.maxY + self.minY) / 2


def is_border(im, pixel):
    (x, y) = pixel
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            x1 = x + dx
            y1 = y + dy
            if 0 <= x1 < height and 0 <= y1 < width:
                if im[x1, y1] == WHITE:
                    return True
    return False


def fill_color(im, pixel, color, only_border=False, compute_box=False):
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
                                (not only_border or is_border(im, (x1, y1))):
                            im[x1, y1] = color
                            queue.append((x1, y1))

    if compute_box:
        return box, total_pixels
    else:
        return total_pixels


img = cv2.imread(sys.argv[1], 0)
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
            fill_color(im_bw, (x, y), WHITE)
            print("Node filtered")

for y in [0, width - 1]:
    for x in range(height):
        if im_bw[x, y] == BLACK:
            fill_color(im_bw, (x, y), WHITE)
            print("Node filtered")

graph = nx.Graph()
id = 0

for x in range(height):
    for y in range(width):
        if im_bw[x, y] == BLACK and is_border(im_bw, (x, y)):
            box, outline = fill_color(im_bw, (x, y), GREY, only_border=True, compute_box=True)
            area = fill_color(im_bw, (x, y), GREY_MARKED)
            node = Node(id, box.get_pos(), outline, area)
            graph.add_node(node)
            print("New node found", node.id, "With area", node.area, "With outline", node.outline, "With pos", node.pos)
            id += 1

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
