import cv2
import mediapipe as mp
import argparse


def detectFace(image, H, W):
    # Detect the face
    mp_face_detection = mp.solutions.face_detection
    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detector:
        img_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        out = face_detector.process(img_RGB)
        if out.detections:
            for face in out.detections:
                location_data = face.location_data
                bbox = location_data.relative_bounding_box
                x, y, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height
                x = int(x * W)
                y = int(y * H)
                w = int(w * W)
                h = int(h * H)
                # print(x, y, w, h)
                # cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

                # Blur the face
                image[y:y + h, x:x + w, :] = cv2.blur(image[y:y + h, x:x + w, :], (50, 50))


args = argparse.ArgumentParser()
args.add_argument("--mode", default="camera")
args.add_argument("--filePath", default="../data/avatar.jpg")

args = args.parse_args()

if args.mode in ["image"]:
    # Read an image
    image = cv2.imread(args.filePath)
    H, W, _ = image.shape
    detectFace(image, H, W)

    # Save image
    cv2.imshow("avatar", image)
    cv2.waitKey(0)

elif args.mode in ["camera"]:
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    ret, frame = cap.read()
    output_video = cv2.VideoWriter("../data/output_video.mp4",
                                   cv2.VideoWriter_fourcc(*'MP4V'),
                                   10,
                                   (frame.shape[1], frame.shape[0]))

    while True:

        H, W, _ = frame.shape
        detectFace(frame, H, W)

        # Save image
        output_video.write(frame)
        cv2.imshow("avatar", frame)
        ret, frame = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    output_video.release()
    cv2.destroyAllWindows()