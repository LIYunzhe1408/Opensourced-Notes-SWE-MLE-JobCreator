import cv2
import os

# read image
image_path = os.path.join('.', 'data', 'rune', 'rune.png')
image = cv2.imread(image_path)
print(image.shape)
image = image[280:650, 720:1200]


img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 501, 0)


cv2.imshow("rune", image)
cv2.imshow("rune-thresh-adaptive", thresh)
cv2.waitKey(0)