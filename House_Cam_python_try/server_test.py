from flask import Flask, render_template, Response, stream_with_context
from dotenv import load_dotenv
from concurrent.futures import ProcessPoolExecutor
import threading
import Queue as queue
import os
import cv2
import time

#dotenv
load_dotenv(verbose=True)
#RTSP
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
#HTTP WEB
app = Flask(__name__, static_folder="/static" , static_url_path="/static")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
#Vars
cam = os.getenv("CAM0")
frame = None
q = queue.Queue(maxsize=2)
#executor = ProcessPoolExecutor(max_workers=2)
#lock = multiprocessing.Manager().Lock()
camera = cv2.VideoCapture(cam)  # use 0 for web camera
camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)
#  for rtsp onvif camera use rtsp://username:password@ip_address:554/onvif1


def gen_frames():  # generate frame by frame from camera
    while True:
        try:
            success, frame = camera.read()
            if not success:
                break
            ret, buffer = cv2.imencode('.jpeg', frame)
            if not ret:
                continue
            buffer = buffer.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + buffer + b'\r\n')  # concat frame one by one and show result
        except:
            print("$4d fr4m3")
            break


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(stream_with_context(gen_frames()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='192.168.0.155', port=80)#threaded=True,
