import cv2
import os

# read image
image_path = os.path.join('.', 'data', 'rune', 'rune.png')
image = cv2.imread(image_path)
print(image.shape)

# Line
cv2.line(image, (820, 500), (850, 500), (0, 255, 0), 2)
cv2.line(image, (825, 505), (845, 505), (0, 255, 0), 2)
cv2.line(image, (830, 510), (840, 510), (0, 255, 0), 2)
cv2.line(image, (835, 500), (835, 515), (0, 255, 0), 2)

# Rectangle
cv2.rectangle(image, (780, 280), (1120, 620), (0, 0, 255), 2)

# Circle
cv2.circle(image, (835, 500), 100, (0, 255, 0), 8)

# Text
cv2.putText(image, "Red Rune Detected", (780, 270), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

cv2.imshow("rune", image)
cv2.waitKey(0)