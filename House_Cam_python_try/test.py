import cv2
import os, sys

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

try:
    cv2.namedWindow("cam0", cv2.WINDOW_NORMAL)
    cam="rtsp://admin:pass@192.168.0.12:554/onvif1"
    cap = cv2.VideoCapture(cam)
    cv2.resizeWindow("cam0", 600, 480)
except:
    print("Connection error")
while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow("cam0", frame)
    print(sys.getsizeof(frame))
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

print("bye!")
