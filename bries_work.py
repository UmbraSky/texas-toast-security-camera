
import cv2
import time
import datetime
from converter import cvimage_to_pygame

def briesStuff(recording, firstRun, cap=None,  face_cascade=None,  body_cascade=None,  detection=None,  detection_stopped_time=None, timer_started=None,  SECONDS_TO_RECORD_AFTER_DETECTION=None,  frame_size=None, fourcc=None, out=None):

    if firstRun == True:
        # pip install opencv-python
        # captured videos will be saved where this python file is saved

        # accesses and activates video camera
        cap = cv2.VideoCapture(0)       # can increment the 0 for different screens

        # default functions for face and body detection
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

        detection = False
        detection_stopped_time = None
        timer_started = False
        SECONDS_TO_RECORD_AFTER_DETECTION = 5

        # size of the camera window
        frame_size = (int(cap.get(3)), int(cap.get(4)))

        # format to save video
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        firstRun = False


    # read each frame from video and display them all together
    _, frame = cap.read()

    # face_cascade and body_cascade require a grayscale image to detect faces/bodies
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)     # 1.3 is accuracy variable. 1 is more accurate but slow. 1.5 is less accurate but fast. 5 is the minimum number of "boxes" for facial detection. if its picking up too many faces, go up an integer. if picking up too few faces, go down
    bodies = body_cascade.detectMultiScale(gray, 1.3, 5)

    # if any body or faces is detected, 
    if len(faces) + len(bodies) > 0:            # dont stop recording until it's been 5 seconds since a face was last detected
        if detection:
            timer_started = False
        else:
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")    #day, month, year, hour, minute, second

            # create an output stream where we write all of the content to
            out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20, frame_size)    
            print("Started recording...")
    elif detection:
        if timer_started:
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                timer_started = False
                out.release()
                print("Stopped recording")
        else:
            timer_started = True
            detection_stopped_time = time.time()

    if detection:
        # write all of the frames of the output stream
        out.write(frame)

    # title of camera window
    #cv2.imshow("Camera", frame)

    # if the "q" key is pressed, the program quits
    if cv2.waitKey(1) == ord('q'):
        recording = False

    if recording == False:
        # save video
        try:
            out.release()
        except:
            pass

        # releases the camera for use elsewhere after stopping program
        cap.release()

        # delete camera window
        cv2.destroyAllWindows()
    
    return cvimage_to_pygame(frame), firstRun, cap,  face_cascade,  body_cascade,  detection,  detection_stopped_time, timer_started,  SECONDS_TO_RECORD_AFTER_DETECTION,  frame_size, fourcc, out
