# The face is detected and regions of interest (ROIs) on the face are identified.
# The coordinates of key points on the face are extracted.
# This process is known as face meshing.

# How is this process done?
    # First, the face is detected and cropped.
    # Then, feature extraction is performed to identify regions of interest (eyes, eyebrows, nose, lips, etc.).
    # Finally, meshing is applied to these ROIs.

import cv2
import mediapipe as mp 
import time

cap = cv2.VideoCapture("3_Goruntu isleme Projeleri/6_face_mesh/video3.mp4")

mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
mpDraw = mp.solutions.drawing_utils
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1) # Since we are meshing the face, the meshing process will not be visible if the faces are far away.
# circle_radius -> the corner points in the skeleton view. 

pTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = faceMesh.process(imgRGB)
    #print(results.multi_face_landmarks)
    
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_TESSELATION, drawSpec, drawSpec)
            #mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_CONTOURS, drawSpec, drawSpec)
      
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    cv2.putText(img, "FPS: "+str(int(fps)), (10,65), cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
    
    cv2.imshow("image", img)
    cv2.waitKey(10)
