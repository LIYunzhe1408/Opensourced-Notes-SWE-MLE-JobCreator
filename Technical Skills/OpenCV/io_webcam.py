import cv2


webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)


ret = True
while ret:
    ret, frame = webcam.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()