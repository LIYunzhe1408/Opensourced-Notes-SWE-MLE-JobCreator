import cv2
import os

# read image
image_path = os.path.join('.', 'data', 'rune', 'rune.png')
image = cv2.imread(image_path)

# The first parameter in the size para is width, which is inverse with the nparray shape.
resized_image = cv2.resize(image, (960, 540))

print(image.shape)
print(resized_image.shape)

cv2.imshow("rune", image)
cv2.imshow("rune-resized", resized_image)
cv2.waitKey(0)