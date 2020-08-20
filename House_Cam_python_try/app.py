from flask import Flask, render_template, Response, stream_with_context
from dotenv import load_dotenv
#from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Process
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
q = queue.Queue(maxsize=1)
READ = False
#executor = ProcessPoolExecutor(max_workers=2)
#lock = multiprocessing.Manager().Lock()
#  for rtsp onvif camera use rtsp://username:password@ip_address:554/onvif1


def gen_frames():  # generate frame by frame from camera
    global q
    ttl = time.time()
    print("New conncetion... wait a second")
    time.sleep(3)
    while True:
        try:
            if q.empty():
                counter = time.time() - ttl
                if (counter) > 3:
                    break
                #time.sleep(1)
                #print("empty queue" + str(counter))
                continue
            else:
                ttl = time.time()
                #print(ttl)
                ret, buffer = cv2.imencode('.jpeg', q.get())
            if not ret:
                continue
            else:
                buffer = buffer.tobytes()
                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + buffer + b'\r\n')  # concat frame one by one and show result
        except:
            print("$4d fr4m3")
            break

def read_frame():
    global q, cam
    camera = cv2.VideoCapture(cam)  # use 0 for web camera
    camera.set(cv2.CAP_PROP_BUFFERSIZE, 5)
    ttl = time.time()
    while True:
        try:
            success, frame = camera.read()
            if not success:
                counter = time.time() - ttl
                if (counter) > 3:
                    print("Bad frame")
                    break
                #time.sleep(1)
                continue
            if q.full():
                #print("ayura")
                counter = time.time() - ttl
                #print(counter)
                if (counter) > 10:
                    print("ay!")
                    break
            else:
                ttl = time.time()
                q.put(frame)
                #print("Put frame to queue")
        except:
            print("Bad connection... Aborting process")
            break
            
    camera.release()

def send_frame(lock):
    global frame
    with lock:
        ret, buffer = cv2.imencode('.jpeg', frame)
        #frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + bytearray(buffer) + b'\r\n')  # concat frame one by one and show result

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(),#stream_with_context(gen_frames()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    try:
        threading.Thread(target=read_frame).start()
        #server = Process(app.run, args=("192.168.0.155", "80"))
        #server.start()
        app.run(host='192.168.0.155', port=80)#, threaded=True
        while True:
            pass
            #time.sleep(0.1)
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        #server.terminate()
        #server.join()
        
#sudo lsof -i :80