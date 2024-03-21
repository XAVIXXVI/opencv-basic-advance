import cv2 as cv

img = cv.imread("photos/cats.jpg")
cv.imshow("Cats", img)

# Averaging
average = cv.blur(img, (3, 3))
cv.imshow("Average Blur", average)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow("Gaussian Blur", gaussian)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median)

# Bilateral Blur
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("Bilateral", bilateral)


cv.waitKey(0)
