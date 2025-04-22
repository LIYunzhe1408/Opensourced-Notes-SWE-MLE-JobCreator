import cv2
import numpy as np


def getLimit(color):
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    print(hsvC)

    lower_limit = hsvC[0][0][0] - 10, 100, 100
    upper_limit = hsvC[0][0][0] + 10, 255, 255

    print(lower_limit, upper_limit)

    lower_limit = np.array(lower_limit, dtype=np.uint8)
    upper_limit = np.array(upper_limit, dtype=np.uint8)

    return lower_limit, upper_limit