"""
Essential functions in OpenCV
"""

import cv2 as cv

img = cv.imread('opencv/photos/cat.jpg')

cv.imshow('Cat', img)

# converting an image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)


# Blur
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)


# Edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow("Edge", canny)


# Dilating the image
dilated = cv.dilate(canny, (5, 5), iterations=3)
cv.imshow("dilated", dilated)


# Eroding
eroded = cv.erode(dilated, (5, 5), iterations=3)
cv.imshow("eroded", eroded)


# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resize", resized)


# Cropping
cropped = img[50:300, 300:500]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
