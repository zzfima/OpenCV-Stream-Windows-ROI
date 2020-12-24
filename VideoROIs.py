import cv2

#  1  |  2
# ----|----
#  3  |  4

capture = cv2.VideoCapture('snake.mp4')
c = 0
is_move_down = True
while True:
    if capture.isOpened():
        (status, frame) = capture.read()

        if not status:
            capture = cv2.VideoCapture('snake.mp4')
            (status, frame) = capture.read()

        cropped_frame_1 = frame[c: c + 200, c: c + 200]
        cropped_frame_2 = frame[c + 200: c + 400, c: c + 200]
        cropped_frame_3 = frame[c: c + 200, c + 200: c + 400]
        cropped_frame_4 = frame[c + 200: c + 400, c + 200: c + 400]

        cv2.imshow('1', cropped_frame_1)
        cv2.imshow('2', cropped_frame_2)
        cv2.imshow('3', cropped_frame_3)
        cv2.imshow('4', cropped_frame_4)
        key = cv2.waitKey(2)
        if is_move_down:
            c += 1
        else:
            c -= 1

        if c == 0:
            is_move_down = True
        elif c + 400 == int(frame.shape[0]) or c + 400 == (frame.shape[1]):
            is_move_down = False
