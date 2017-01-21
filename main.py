import numpy as np
import cv2
import sys

def process(frame):
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    return gray

img = cv2.imread(sys.argv[1], 0)
ret,thresh1 = cv2.threshold(img,180,255,cv2.THRESH_BINARY)


#out = process(img)

cv2.imshow('frame', thresh1)


# Wait for quit key
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cv2.destroyAllWindows()
