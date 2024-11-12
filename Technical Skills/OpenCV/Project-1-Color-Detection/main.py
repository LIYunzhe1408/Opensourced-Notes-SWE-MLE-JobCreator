import cv2
from utils import getLimit
from PIL import Image


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
yellow = [0, 255, 255] # This is yellow in BGR

while True:
    ret, frame = cap.read()

    HSV_Image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerBound, upperBound = getLimit(color=yellow)
    mask = cv2.inRange(HSV_Image, lowerBound, upperBound)
    mask_ = Image.fromarray(mask)

    bbox_ = mask_.getbbox()
    if bbox_ is not None:
        x1, y1, x2, y2 = bbox_
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

    cv2.imshow("frame", frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()