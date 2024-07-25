import cv2
import os

# read image
image_path = os.path.join('.', 'data', 'scooter', '5.jpg')
image = cv2.imread(image_path)

# write image
cv2.imwrite(os.path.join('.', 'data', 'scooter_out.jpg'), image)

# visualize image
cv2.imshow("frame", image)
cv2.waitKey(0)