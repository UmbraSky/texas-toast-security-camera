
import cv2
import time
import datetime
from flask import session

def briesVars():

    # pip install opencv-python
    # captured videos will be saved where this python file is saved

    # accesses and activates video camera
    session["cap"] = cv2.VideoCapture(0)       # can increment the 0 for different screens

# default functions for face and body detection
    session["face_cascade"] = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    session["body_cascade"] = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

    session["detection"]= False
    session["detection_stopped_time"] = None
    session["timer_started"] = False
    session["SECONDS_TO_RECORD_AFTER_DETECTION"] = 5

    # size of the camera window
    session["frame_size"] = (int(session["cap"].get(3)), int(session["cap"].get(4)))

    # format to save video
    session["fourcc"] = cv2.VideoWriter_fourcc(*"mp4v")

def briesLoop():
    while True:
        # read each frame from video and display them all together
        _, frame = session["cap"].read()

        # face_cascade and body_cascade require a grayscale image to detect faces/bodies
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = session["face_cascade"].detectMultiScale(gray, 1.3, 5)     # 1.3 is accuracy variable. 1 is more accurate but slow. 1.5 is less accurate but fast. 5 is the minimum number of "boxes" for facial detection. if its picking up too many faces, go up an integer. if picking up too few faces, go down
        bodies = session["body_cascade"].detectMultiScale(gray, 1.3, 5)

        # if any body or faces is detected, 
        if len(faces) + len(bodies) > 0:            # dont stop recording until it's been 5 seconds since a face was last detected
            if session["detection"]:
                session["timer_started"] = False
            else:
                session["detection"]= True
                current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")    #day, month, year, hour, minute, second

                # create an output stream where we write all of the content to
                session["out"] = cv2.VideoWriter(f"{current_time}.mp4", session["fourcc"], 20, session["frame_size"])    
                print("Started recording...")
        elif session["detection"]:
            if session["timer_started"]:
                if time.time() - session["detection_stopped_time"] >= session["SECONDS_TO_RECORD_AFTER_DETECTION"]:
                    session["detection"]= False
                    session["timer_started"] = False
                    session["out"].release()
                    print("Stopped recording")
            else:
                session["timer_started"] = True
                session["detection_stopped_time"] = time.time()

        if session["detection"]:
            # write all of the frames of the output stream
            session["out"].write(frame)

        # title of camera window
        #cv2.imshow("Camera", frame)

        # if the "q" key is pressed, the program quits
        if cv2.waitKey(1) == ord('q'):
            break
    
    # Brie had this code outside the while True loop. I moved it into a function
    # so that it could be accessed from other files.

    # save video
    session["out"].release()

    # releases the camera for use elsewhere after stopping program
    session["cap"].release()

    # delete camera window
    cv2.destroyAllWindows()
    

    
