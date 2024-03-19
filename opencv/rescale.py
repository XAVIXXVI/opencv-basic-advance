"""
Re-size and re-scale images and video frames.
"""
import cv2 as cv


def rescale_frame(frame, scale):
    """Re-size the frame"""

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def re_size_video(file_path, scale=0.75):
    """Reads the video and resize it."""

    capture = cv.VideoCapture(file_path)
    while True:
        isTrue, frame = capture.read()
        frame_resized = rescale_frame(frame, scale)
        cv.imshow('Re-sized Video', frame_resized)
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    capture.release()
    cv.destroyAllWindows()
    return None


def re_size_image(file_path, scale=0.75):
    """Reads the image and resize it."""

    img = cv.imread(file_path)
    rezied_img = rescale_frame(img, scale)
    cv.imshow("Re-sized image", rezied_img)
    cv.imshow("Image", img)
    cv.waitKey(0)
    return None


# def change_res(width, height):
#     """this will not work on already existing video files and
#     only works on live video"""

#     capture.set(3, width)
#     capture.set(4, height)


if __name__ == "__main__":

    # re_size_video("opencv\\videos\\dog.mp4")
    re_size_image('opencv\\photos\\cat_large.jpg', 0.25)
