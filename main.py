import cv2
import pyautogui
import numpy as np

from find_ball import find_ball
from find_targeting_line import find_targeting_line

# change depending on game screen size
game_res = [1152, 720]
border = [0, 20]

# threshold = 0.95

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

        # cut out the bottom middle third of the screen as ROI for the ball
        ball_roi = img[int(img.shape[0] / 2): img.shape[0], int(img.shape[1] * 1 / 3): int(img.shape[1] * 2 / 3)]

        # insert the ball ROI back into the full image
        img[int(img.shape[0] / 2): img.shape[0], int(img.shape[1] * 1 / 3): int(img.shape[1] * 2 / 3)] = find_ball(ball_roi)

        # cut out the bottom middle third of the screen as ROI for the targeting line
        targeting_line_roi = img[0: img.shape[0], int(img.shape[1] * 1 / 3): int(img.shape[1] * 2 / 3)]

        # insert the targeting line ROI back into the full image
        img[0: img.shape[0], int(img.shape[1] * 1 / 3): int(img.shape[1] * 2 / 3)] = find_targeting_line(targeting_line_roi)

        cv2.imshow('image', img)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            raise KeyboardInterrupt

except KeyboardInterrupt:
    import os
    import glob

    cv2.destroyAllWindows()

    for file in glob.glob('..screen.png*'):
        os.remove(file)

    os.remove('screen.png')

