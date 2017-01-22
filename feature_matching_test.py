from Queue import PriorityQueue

import numpy as np
import cv2
from matplotlib import pyplot as plt
import os

IMG_BASEPATH = 'test_images'


def compute_matches(path_obj, path_scene, threshold=12):
    # Feature matching
    img1 = cv2.imread(path_obj, 0)  # queryImage
    img2 = cv2.imread(path_scene, 0)  # trainImage

    # Initiate ORB detector
    orb = cv2.ORB_create(edgeThreshold=9)
    # find the keypoints and descriptors with ORB
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    # Match descriptors.
    matches = bf.match(des1, des2)
    # Sort them in the order of their distance.
    matches = sorted(matches, key=lambda x: x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:30], flags=2, outImg=8)

    return matches, img3


if __name__ == "__main__":
    gus_patt_predict = os.path.join(IMG_BASEPATH, 'gus_pattern_predict.png')
    gus_patt = os.path.join(IMG_BASEPATH, 'pattern_gus.png')

    predict = gus_patt_predict
    predict = os.path.join(IMG_BASEPATH, 'gus_photo_1.png')
    pattern = gus_patt

    matches, img = compute_matches(predict, pattern)
    print "We found %d matches!" % len(matches)
    print "%d of them have 0 distance to Gus' pattern." % len([x for x in matches if x.distance == 0])
    print min(matches, key=lambda x: x.distance).distance

    plt.imshow(img), plt.show()