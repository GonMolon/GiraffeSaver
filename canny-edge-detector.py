import cv2
import numpy as np
import sys

img = cv2.imread(sys.argv[1],0)
edges = cv2.Canny(img,100,200)

cv2.imshow("hi", edges)





# Wait for quit key
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
