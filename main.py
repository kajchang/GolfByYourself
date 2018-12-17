import cv2
import pyautogui
import numpy as np

# change depending on game screen size
game_res = [1152, 720]
border = [0, 20]

ball = cv2.imread('templates/Ball.png', 0)

threshold = 0.95

try:
    while True:
        img = cv2.cvtColor(
            np.array(
                pyautogui.screenshot('screen.png', region=(border[0],
                                                           border[1],
                                                           game_res[0] + border[0],
                                                           game_res[1] + border[1]))),
            cv2.COLOR_BGR2GRAY
        )

        top = img[0: int(img.shape[0] / 2), 0: img.shape[1]]
        bottom = img[int(img.shape[0] / 2): img.shape[0], 0: img.shape[1]]

        res = cv2.matchTemplate(bottom, ball, cv2.TM_CCORR_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        w, h = ball.shape[::-1]

        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(bottom, top_left, bottom_right, 0, 2)

        cv2.imshow('image', np.concatenate((top, bottom), axis=0))

        if cv2.waitKey(25) & 0xFF == ord('q'):
            raise KeyboardInterrupt

except KeyboardInterrupt:
    import os
    import glob

    cv2.destroyAllWindows()

    for file in glob.glob('..screen.png*'):
        os.remove(file)

    os.remove('screen.png')

