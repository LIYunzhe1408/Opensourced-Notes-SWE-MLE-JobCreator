import numpy as np
import cv2
import os

# read image
image_path = os.path.join('.', 'data', 'rune', 'rune.png')
image = cv2.imread(image_path)
print(image.shape)
image = image[280:650, 720:1200]

edge_detector = cv2.Canny(image, 200, 400)
edge_detector_dilate = cv2.dilate(edge_detector, np.ones((3, 3)))
edge_detector_erode = cv2.erode(edge_detector_dilate, np.ones((3, 3)))

cv2.imshow("rune", image)
cv2.imshow("rune-edge_detector", edge_detector)
cv2.imshow("rune-edge_detector_dilate", edge_detector_dilate)
cv2.imshow("rune-edge_detector_erode", edge_detector_erode)
cv2.waitKey(0)