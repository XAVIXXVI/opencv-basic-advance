"""
Reading photos and videos using opencv.
"""
import cv2 as cv


def read_image(file_path):
    img = cv.imread(file_path)
    cv.imshow("cat", img)
    cv.waitKey(0)
    return None


def read_video(file_path):
    capture = cv.VideoCapture(file_path)
    while True:
        isTrue, frame = capture.read()
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    capture.release()
    cv.destroyAllWindows()
    return None


if __name__ == "__main__":

    read_video("opencv\\videos\\dog.mp4")
    # read_image('opencv\\photos\\cat_large.jpg')
