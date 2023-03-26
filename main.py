# #thank you Jesus

#imprting necessary libraries
import cv2 #for Computer vision. It triggers the Webcam of your local machine
import mediapipe as mp  # a python library that can identify and measure landmarks on human body
import csv #for reading the filters annotation files
import numpy as np #for arrays and managing the points
import math 

#Let's set up a small unregular api that can fetch our filter image as well as their annotations and properties(alpha and morph)
#images are usually in RGB but some images have 'alpha' which controls the transparency 

# filters_API = {
#     'rainbowmouthfilter':
#         [{'png_path': "filters_folder/rainbowmouthfilter.png",
#           'annotation_file': "filters_folder/rainbowmouthfilter.csv",
#           'morph': True, 'animated': False, 'has_alpha': True}],
#     'nosemask_ears_filter':
#         [{'path': "filters_folder/nosemask_ears_filter.png",
#           'annotation_file': "filters_folder/nosemask_ears_filter.csv",
#           'morph': True, 'animated': False, 'has_alpha': True}],
#     'fowerfilter':
#         [{'path': "filters_folder/fowerfilter.png",
#           'annotation_file': "filters_folder/fowerfilter.csv",
#           'morph': False, 'animated': False, 'has_alpha': True}],
#     'moustache_filter':
#         [{'path': "filters_folder/moustache_filter.png",
#           'annotation_file': "filters_folder/moustache_filter.csv",
#           'morph': False, 'animated': False, 'has_alpha': True}],
#     'heartfilter':
#         [{'path': "filters_folder/heartfilter.png",
#           'annotation_file': "filter_folder/heartfilter.csv",
#           'morph': True, 'animated': False, 'has_alpha': True}],
#     'glasses_filter':
#         [{'path': "filters_folder/glasses_filter.png",
#           'annotation_file': "filters_folder/glasses_filter.csv",
#           'morph': False, 'animated': False, 'has_alpha': True}],
#     'dog_ears_nose_filter':
#         [{'path': "filters_folder/dog_ears_nose_filter.png",
#           'annotation_file': "filters_folder/dog_ears_nose_filter.csv",
#           'morph': False, 'animated': False, 'has_alpha': True}],
#     'cutebunny_filter':
#         [{'path': "filters_folder/cutebunny_filter.png",
#           'annotation_file': "filters_folder/cutebunny_filter.csv",
#           'morph': False, 'animated': False, 'has_alpha': True}],
#     'cityfilter':
#         [{'path': "filters_folder/cityfilter.png",
#           'annotation_file': "filters_folder/cityfilter.csv",
#           'morph': False, 'animated': False, 'has_alpha': True}],
#     'butterfly_filter':
#         [{'path': "filters_folder/butterfly_filter.png",
#           'annotation_file': "filters_folder/butterfly_filter.csv",
#           'morph': False, 'animated': False, 'has_alpha': True}],
#     'bulgyeyes_filter':
#         [{'path': "filters_folder/bulgyeyes_filter.png",
#           'annotation_file': "filters_folder/bulgyeyes_filter.csv",
#           'morph': False, 'animated': False, 'has_alpha': True}],
#           #remains angel_filter and blueflower_filter.png
    
# }

mp_face_mesh = mp.solutions.face_mesh  # identifies and defines the landmarks and points on your face
def get_face_landmarks(img):
    """ This function gets Mediapipe facial landmarks, processes it on the image, converts it into an array and 
    maps the array coordinates in form of an image getting all the important points on the face.
    The purpose of this function is to get facial landmarks with media pipe landmarks as a guide"""

    mp_face_mesh = mp.solutions.face_mesh  # identifies and defines the landmarks and points on your face
    mp_keypoints = [127, 93, 58, 136, 150, 149, 176, 148, 152, 377, 400, 378, 379, 365, 288, 323, 356, 70, 63, 105, 66, 55,
                 285, 296, 334, 293, 300, 168, 6, 195, 4, 64, 60, 94, 290, 439, 33, 160, 158, 173, 153, 144, 398, 385,
                 387, 466, 373, 380, 61, 40, 39, 0, 269, 270, 291, 321, 405, 17, 181, 91, 78, 81, 13, 311, 306, 402, 14,
                 178, 162, 54, 67, 10, 297, 284, 389]
    h,w = img.shape[:-1] #setting up the dimensions of the width and height ofthe image
    #setting the face mesh to taste
    with mp_face_mesh.FaceMesh(
        max_num_faces = 1, #You can change to 2 if you want
        refine_landmarks = True,
        min_detection_confidence = 0.8,
        static_image_mode = True,
        min_tracking_confidence = 0.5) as face_mesh:

        #to convert the image from grayscale to (red green blue)type image
        results = face_mesh.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        #if python is unable to find any image to convert from grayscale to RGB it will print unable to detect
        #any face
        if results.multi_face_landmarks == False:
            print("Unable to detect Face")
            return 0
        
        #if a facial image is detected, the points on the face should be converted to an array
        for faceLandmarks in results.multi_face_landmarks:
            array_values = np.array(faceLandmarks.landmark)
            face_points = np.zeros((len(array_values), 2)) #to create a zero array for the face landmarks detected
        
        #To iterate through the array values, assigning id numbers to them
        for idx, value in enumerate(array_values):
                face_points[idx][0] = value.x
                face_points[idx][1] = value.y

        #mapping the face_points to image coordinates
        face_points = face_points * (w, h)
        face_points = face_points.astype('int')

        keypoints = []

        for i in mp_keypoints:
            keypoints.append(face_points[i])
        return keypoints
    return 0

#function for loading the filter images from the filter folders
#We're passing in an 'has_alpha in case the image has transparency
def load_filter_images(img_path, has_alpha):
    """ This func loads the filter images from a path, splits it into several components, gets rid of the 
    alpha channel, remerge and returns seperately the image and the alpha"""
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED) #to load the filter image from it's path
    alpha = None
    if has_alpha:
        r, g, b, alpha = cv2.split(img) #to split the image into several single channeled      images
        img = cv2.merge((r, g, b)) # The purpose of this is to 
        #remerge the single channnel images getting rid of the alpha(transparency in the filter image)

    return img, alpha
     
def load_landmarks(annotation_file):
    """ This function gets the annotation file of each filter images and extracts the x and y 
    landmark coordinates returning the points when called"""
    with open(annotation_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        points = {}
        for i, j in enumerate(csv_reader):
            try:
                x, y = int(j[1]), int(j[2])
                points[j[0]] = (x, y)
            except ValueError:
                continue
        return points
        
def get_convex_points(points):
    """ Convex points or CV2convexhull are points or places in the face or body that are bounded together 
    forming a closed shape(regular or irregular) e.g includes the eyes, lips, nose, eyebrows, beards etc 
    apart from the face, the convex points could include a polygon, cars, etc... as long as its a closed shape
    with boundaries. This func enabes python to be aware of hull points in the face in order to be able to
    fit the filter on the face much better"""
    convex_points = [] #list of convex points

    #To find the convex hull of our points array
    convex_points_index = cv2.convexHull(np.array(list(points.values())), returnPoints=False, clockwise=False,)
    facial_hull_points = [
        #hull points of the eyes, nose, eyebrows, and lips
        [17], [18], [19], [20], [21], [22], [23], [24], [25], [26],
        [27], [28], [29], [30], [31], [32], [33], [34], [35],  
        [48], [49], [50], [51], [52], [53], [54], [55], [56], [57], [58], [59]
        [36], [37], [38], [39], [40], [41], [42], [43], [44], [45], [46], [47], 
        [60], [61], [62], [63], [64], [65], [66], [67], 
          
    ]
    convex_points_index = np.concatenate((convex_points_index, facial_hull_points))
    for i in range(0, len(convex_points_index)):
        convex_points.append(points[str(convex_points_index[i][0])])

    return convex_points, convex_points_index
    
  

