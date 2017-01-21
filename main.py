import cv2
import sys
import networkx as nx


class Node:
    def __init__(self, id, area):
        self.id = id
        self.area = area


def is_border(im, pixel):
    (x, y) = pixel
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if (dx != 0 or dy != 0) and (dx == 0 or dy == 0):
                if im[x, y] == WHITE:
                    return True
    return False


def fill_color(im, pixel, color):
    total_pixels = 0
    org = im[pixel]
    queue = [pixel]

    while queue:
        (x, y) = queue[0]
        queue.pop(0)
        total_pixels += 1
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (dx != 0 or dy != 0) and (dx == 0 or dy == 0):
                    x1 = x + dx
                    y1 = y + dy
                    if 0 <= x1 < height and 0 <= y1 < width:
                        if im[x1, y1] == org and is_border(im, (x1, y1)):
                            im[x1, y1] = color
                            queue.append((x1, y1))

    return total_pixels


img = cv2.imread(sys.argv[1], 0)
ret, im_bw = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)

height, width = img.shape
print(height)
print(width)


WHITE = 255
GREY = 128
BLACK = 0

for x in [0, height-1]:
    for y in range(width):
        if im_bw[x, y] == BLACK:
            fill_color(im_bw, (x, y), WHITE)

for y in [0, width-1]:
    for x in range(height):
        if im_bw[x, y] == BLACK:
            fill_color(im_bw, (x, y), WHITE)

graph = nx.Graph()
id = 0

for x in range(height):
    for y in range(width):
        if im_bw[x, y] == BLACK:
            area = fill_color(im_bw, (x, y), GREY)
            graph.add_node(Node(id, area))
            id += 1


cv2.imshow('pattern', im_bw)

# Wait for quit key
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cv2.destroyAllWindows()
