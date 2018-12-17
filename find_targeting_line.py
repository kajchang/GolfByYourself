import cv2
import numpy as np


def find_targeting_line(roi):
    edges = cv2.Canny(roi, 200, 300)

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, 25, 20)

    if lines is None:
        return roi

    for line in lines:
        coords = line[0]
        cv2.line(roi, (coords[0], coords[1]), (coords[2], coords[3]), 0, 5)

    return roi
