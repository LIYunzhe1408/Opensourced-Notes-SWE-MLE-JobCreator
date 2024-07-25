import os
import cv2

video_path = os.path.join('.', 'rune', '大能量机关8m正在激活状态灯效.mp4')
video = cv2.VideoCapture(video_path)

ret = True
while ret:
    ret, frame = video.read()
    if ret:
        cv2.imshow('Rune', frame)
        cv2.waitKey(40)

video.release()
cv2.destroyAllWindows()