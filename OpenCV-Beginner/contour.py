import numpy as np
import cv2
import os

# read image
image_path = os.path.join('.', 'data', 'rune', 'rune.png')
image = cv2.imread(image_path)
print(image.shape)
image = image[280:650, 720:1200]

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(image_gray, 200, 255, cv2.THRESH_BINARY)
thresh = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 301, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt) < 2000 and cv2.contourArea(cnt) > 1000:
        cv2.drawContours(image, cnt, -1, (0, 255,0), 3)
        x1, y1, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(image, (x1, y1), (x1+w, y1+h), (0, 255, 0), 2)

cv2.imshow("rune", image)
cv2.imshow("thresh", thresh)
cv2.waitKey(0)