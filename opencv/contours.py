"""
Contour detection
"""
import cv2 as cv
import numpy as np


img = cv.imread("opencv/photos/cats.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("Blank image", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray cats", gray)

# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow("Blur cats", gray)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow("canny", canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresholded image", thresh)

contours, hierarchies = cv.findContours(thresh,
                                        cv.RETR_LIST,
                                        cv.CHAIN_APPROX_NONE)


cv.drawContours(blank, contours, -1, (0, 0, 255), 2)
cv.imshow("Countour drawn", blank)

cv.waitKey(0)
