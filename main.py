import cv2
import sys
import networkx as nx





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






cv2.imshow('pattern', im_bw)

# Wait for quit key
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cv2.destroyAllWindows()
