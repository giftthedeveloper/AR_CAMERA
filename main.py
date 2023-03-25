#thank you Jesus

#importing necessary libraries
import cv2  #for Computer vision. It triggers the Webcam of your local machine
import numpy as np # for array operationss
import mediapipe as mp # a python library that can identify and measure landmarks on human body

mp_drawing = mp.solutions.drawing_utils  #this outlines(draws the skeleton or line frame) and tracks the part of the body you want
mp_drawing_styles = mp.solutions.drawing_styles #defines the pattern of drawing outline
mp_face_mesh = mp.solutions.face_mesh  # identifies and defines the landmarks and points on your face

#setting up the face mesh  to taste
with mp_face_mesh.FaceMesh(
    max_num_faces = 1, #You can change to 2 if you want
    refine_landmarks = True,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5) as face_mesh:

    #setting up the title of the camera window
    img = cv2.imread('filters/facees.jpg', cv2.IMREAD_UNCHANGED)

    #horizontally positionin the screen and converting the video image from 
    # BGR(normal image) TO RGB (computer kind of image)
    image = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)

    #for better performance we'll mark the image as only redeable and non-writeable
    image.flags.writeable = False
    results = face_mesh.process(image)

    #to get the x, y landmark dimensions of the face
    (results.multi_face_landmarks[0].landmark[205].x * image.shape[1],
     results.multi_face_landmarks[0].landmark[205].y * image.shape[1])
