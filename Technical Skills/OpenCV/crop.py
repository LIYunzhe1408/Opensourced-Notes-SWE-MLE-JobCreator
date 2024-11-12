import cv2
import os

# read image
image_path = os.path.join('.', 'data', 'rune', 'rune.png')
image = cv2.imread(image_path)
rune = image[280:620, 760:1150]

print(image.shape)
print(rune.shape)

cv2.imshow("rune", image)
cv2.imshow("rune-crop", rune)
cv2.waitKey(0)