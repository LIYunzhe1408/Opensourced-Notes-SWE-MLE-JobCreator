import cv2
import os

# read image
image_path = os.path.join('.', 'data', 'rune', 'rune.png')
image = cv2.imread(image_path)
print(image.shape)
image = image[280:650, 720:1200]

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)

# thresh = cv2.blur(thresh, (3,3))
# ret, thresh = cv2.threshold(thresh, 180, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("rune", image)
cv2.imshow("rune-thresh-global", thresh)
cv2.waitKey(0)