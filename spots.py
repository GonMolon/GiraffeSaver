import numpy as np
import cv2
import sys


def process(frame):
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    return gray


def spots(img):
    img = cv2.resize(img, (900,600))
    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    img = cv2.medianBlur(img, 3)

    kernel = np.ones((4, 4), np.uint8)
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.medianBlur(img, 7)
    kernel = np.ones((4, 4), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)

    img = cv2.medianBlur(img, 9)
    return img


def test():
    img = cv2.imread(sys.argv[1], 0)
    img = spots(img)
    cv2.imshow('frame', img)

    # Wait for quit key
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cv2.destroyAllWindows()
