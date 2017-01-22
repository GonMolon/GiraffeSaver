import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

MIN_MATCH_COUNT = 10
IMG_BASEPATH = 'test_images'

img1 = cv2.imread(os.path.join(IMG_BASEPATH, 'pattern_gus.png'), 0) # queryImage
img2 = cv2.imread(os.path.join(IMG_BASEPATH, 'gus_photo_1.png'), 0) # trainImage

img = cv2.imread(os.path.join(IMG_BASEPATH, 'pattern_gus.png'), 0) # queryImage

# Create SURF object. You can specify params here or later.
# Here I set Hessian Threshold to 400
surf = cv2.xfeatures2d.SURF_create(400)
# Find keypoints and descriptors directly
kp, des = surf.detectAndCompute(img,None)
print len(kp)

print surf.getUpright()
surf.setUpright(True)
#kp = surf.detect(img,None)
img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)

plt.imshow(img2),plt.show()


# ORB
img = cv2.imread(os.path.join(IMG_BASEPATH, 'pattern_gus.png'), 0) # queryImage
# Initiate ORB detector
orb = cv2.ORB_create(edgeThreshold=12)
# find the keypoints with ORB
kp = orb.detect(img,None)
# compute the descriptors with ORB
kp, des = orb.compute(img, kp)
# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)
plt.imshow(img2), plt.show()

# Feature matching
img1 = cv2.imread(os.path.join(IMG_BASEPATH, 'gus_pattern_predict.png'), 0) # queryImage
img2 = cv2.imread(os.path.join(IMG_BASEPATH, 'pattern_gus.png'), 0) # trainImage

# Initiate ORB detector
orb = cv2.ORB_create(edgeThreshold=12)
# find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# Match descriptors.
matches = bf.match(des1,des2)
# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)
# Draw first 10 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], flags=2, outImg=8)
plt.imshow(img3),plt.show()