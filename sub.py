#thank you Jesus

#importing the necessary library
import cv2   #for Computer vision. It triggers the Webcam of your local machine
import mediapipe as mp  # a python library that can identify and measure landmarks on human body
import numpy as np

mp_drawing = mp.solutions.drawing_utils  #this outlines(draws the skeleton or line frame) and tracks the part of the body you want
mp_drawing_styles = mp.solutions.drawing_styles #defines the pattern of drawing outline
mp_face_mesh = mp.solutions.face_mesh  # identifies and defines the landmarks and points on your face



#defining the style & dimension of drawing
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

# to load the webcam
cap = cv2.VideoCapture(0)

#setting the face mesh to taste
with mp_face_mesh.FaceMesh(
    max_num_faces = 1, #You can change to 2 if you want
    refine_landmarks = True,
    min_detection_confidence = 0.8,
    min_tracking_confidence = 0.5) as face_mesh:

    while cap.isOpened():
        #reading the live video data with cv2
        success, image = cap.read()
        if not success:
            print("Ignored camera frame")

            break
        #for better performance we'll mark the image as only redeable and non-writeable
        image.flags.writeable  = False

        # img = 

        #converting the video image from BGR(normal image) TO RGB (computer kind of image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image)

        #Earlier on, The image.flags.writeable was set to false because we wanted to process for the computer to 
        #read and understand it.the image kind was also converted to RGB and now we would convert it to back to BGR
        #so it can be displayed on our screen and we can see and understand it.

        #draw the face mesh annotations on the image
        image.flags.writeable  = True #this is set to true because we want the face mesh on the face to be visible
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list = face_landmarks,
                    connections = mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec = None,
                    connection_drawing_spec = mp_drawing_styles.get_default_face_mesh_tesselation_style()
                )
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list = face_landmarks,
                    connections = mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec = None,
                    connection_drawing_spec = mp_drawing_styles.get_default_face_mesh_contours_style()
                )
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list = face_landmarks,
                    connections = mp_face_mesh.FACEMESH_IRISES,
                    landmark_drawing_spec = None,
                    connection_drawing_spec = mp_drawing_styles.get_default_face_mesh_iris_style()
                )

        # to flip the image horizontally for a selfie-view display
        cv2.imshow('Face Filter Project', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()



    
    




