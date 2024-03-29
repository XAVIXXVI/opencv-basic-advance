"""
Draw and write on images using opencv
"""
import cv2 as cv
import numpy as np


# img = cv.imread("opencv\photos\cat.jpg")
# cv.imshow('Cat', img)

"""Paint the image a certain colour"""
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow("Blank", blank)

# blank[:] = 0, 255, 0
# cv.imshow('Green', blank)

# """Fill certain region with color"""
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('Fill certain region with color', blank)


# """Draw a rectangle"""
# cv.rectangle(blank, (0, 0), (250, 250), (255, 0, 0), thickness=2)
# cv.imshow("Rectangle without fill", blank)


# """Fill the rectangle with a color"""
# cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2),
#              (255, 0, 0), thickness=-1)
# cv.imshow('Rectangle filled', blank)


# """Draw a circle"""
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),
#           40, (0, 0, 255), thickness=2)
# cv.imshow('Circle', blank)


# """Draw a line"""
# cv.line(blank, (0, 0), (250, 250), (255, 255, 255), thickness=2)
# cv.imshow('Line', blank)

"""Write text in image"""
cv.putText(blank, "Hello, my name is Xavi", (0, 255), cv.FONT_HERSHEY_TRIPLEX,
           1.0, (255, 0, 0), 2)
cv.imshow("Text", blank)


cv.waitKey(0)
