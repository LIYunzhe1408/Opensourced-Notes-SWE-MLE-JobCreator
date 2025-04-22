import cv2
import os

# read image
image_path = os.path.join('.', 'data', 'rune', 'rune.png')
image = cv2.imread(image_path)

image_Gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow("rune", image)
cv2.imshow("rune_Gray", image_Gray)
cv2.imshow("rune_RGB", image_RGB)
cv2.imshow("rune_HSV", image_HSV)

# Save two images in different color space, their storage size different.
# cv2.imwrite("gray_rune.png", image_Gray)
# cv2.imwrite("RGB_rune.png", image_RGB)
# cv2.imwrite("RGB_rune.png", image_HSV)
cv2.waitKey(0)