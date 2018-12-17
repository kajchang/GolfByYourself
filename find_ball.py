import cv2

ball = cv2.imread('templates/Ball.png', 0)


def find_ball(roi):
    # find best match for the ball
    res = cv2.matchTemplate(roi, ball, cv2.TM_CCORR_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # draw a bounding box around the maatch
    w, h = ball.shape[::-1]
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(roi, top_left, bottom_right, 0, 2)

    return roi
