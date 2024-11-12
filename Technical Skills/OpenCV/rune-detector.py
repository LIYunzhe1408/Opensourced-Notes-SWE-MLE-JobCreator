import cv2
import os
import numpy as np


def detectBoundingBox(image):
    image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    image_Red1 = cv2.inRange(image_HSV, (0, 43, 46), (10, 255, 255))
    image_Red2 = cv2.inRange(image_HSV, (170, 43, 46), (180, 255, 255))
    red = cv2.bitwise_or(image_Red1, image_Red2)
    red = cv2.dilate(red, np.ones((7, 7)))

    # Detect the contour and draw its bounding box
    contours, hierarchy = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        print(cv2.contourArea(cnt))
        if cv2.contourArea(cnt) > 6000 and cv2.contourArea(cnt) < 18000:
            # cv2.drawContours(image, cnt, -1, (0, 255,0), 3)
            x1, y1, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(image, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)
    return image


video_path = os.path.join('.', 'data', 'video-rune', '大能量机关8m正在激活状态灯效.mp4')
video = cv2.VideoCapture(video_path)

ret = True
while ret:
    ret, frame = video.read()
    if ret:
        image = detectBoundingBox(frame)
        cv2.imshow('Rune', image)
        if cv2.waitKey(40) & 0xFF == ord('q'):
            break

video.release()
cv2.destroyAllWindows()