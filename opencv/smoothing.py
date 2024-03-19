import cv2 as cv

img = cv.imread("opencv/photos/cats.jpg")
cv.imshow("Cats", img)


cv.waitKey(0)
