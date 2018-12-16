import cv2
import numpy as np

screen = cv2.imread('images/Screen.png', 0)

img = screen.copy()

template = cv2.imread('images/Ball.png', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(img, top_left, bottom_right, 255, 2)

cv2.imwrite('output/bounding_ball.png', img)
