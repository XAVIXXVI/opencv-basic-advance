"""
Basic Image Transformations
"""

import cv2 as cv
import numpy as np

img = cv.imread('opencv/photos/park.jpg')

cv.imshow("Park", img)


# translation
def translate(img, x, y):
    trans_mat = np.float32([[1, 0, x], [0, 1, y]])
    dimentions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans_mat, dimentions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down


translated = translate(img, 100, -100)
cv.imshow("Translated", translated)


# Rotation
def rotate(img, angle, rot_point=None):
    (height, width) = img.shape[:2]

    if rot_point is None:
        rot_point = (width//2, height//2)

    rot_mat = cv.getRotationMatrix2D(rot_point, angle, 1.0)
    dimentions = (width, height)

    return cv.warpAffine(img, rot_mat, dimentions)


rotated = rotate(img, 45)
cv.imshow("Rotated", rotated)


# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)


# Flipping
flip = cv.flip(img, 1)
cv.imshow("Flipped", flip)


# Cropping
cropped = img[200:400, 300:500]
cv.imshow("Cropped", cropped)


cv.waitKey(0)
