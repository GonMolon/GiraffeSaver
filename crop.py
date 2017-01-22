import cv2
import numpy as np

def crop(img, path):
    mask = np.zeros(img.shape, dtype=np.uint8)
    roi_corners = np.array([path], dtype=np.int32)

    # fill the ROI so it doesn't get wiped out when the mask is applied
    channel_count = img.shape[2]  # i.e. 3 or 4 depending on your img
    ignore_mask_color = (255,)*channel_count
    cv2.fillPoly(mask, roi_corners, ignore_mask_color)

    # apply the mask
    img = cv2.bitwise_and(img, mask)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j][0] == 0 and img[i][j][1] == 0 and img[i][j][2] == 0: img[i][j] = [255,]*channel_count

    return img

def test():
    img = cv2.imread('test_images/pattern1.png', -1)
    path = [(100,100), (500,100), (500,500), (100,500), (250,250)]

    img = crop(img, path)

    # save the result
    cv2.imwrite('imgout.jpg', img)

test()
