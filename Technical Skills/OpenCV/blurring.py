import cv2
import os

# read image
image_path = os.path.join('.', 'data', 'rune', 'rune.png')
image = cv2.imread(image_path)

# Define neighbour proximity
k_size = 7
img_blur = cv2.blur(image, (k_size, k_size))
img_gaussian = cv2.GaussianBlur(image, (k_size, k_size), 3)
img_median = cv2.medianBlur(image, k_size)

cv2.imshow("rune", image)
cv2.imshow("rune-blur", img_blur)
cv2.imshow("rune-gaussian", img_gaussian)
cv2.imshow("rune-median", img_median)
cv2.waitKey(0)