
import  cv2
import mediapipe as mp

cap = cv2.VideoCapture("your_file_path")

mpFaceDetection = mp.solutions.face_detection
faceDetection = mpFaceDetection.FaceDetection(0.2)
mpDraw = mp.solutions.drawing_utils

while True:
    success, img  = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = faceDetection.process(imgRGB)
    print(results.detections)
    
    if results.detections:
        for id, detection in enumerate(results.detections):
            bboxC = detection.location_data.relative_bounding_box
            #print(bboxC)
            
            height, width, _ = img.shape
            bbox = int(bboxC.xmin*width), int(bboxC.ymin* height), int(bboxC.width*width), int(bboxC.height*height)
            #print(bbox)
            cv2.rectangle(img, bbox, (0,255,255),2)
    
    cv2.imshow("image",img)
    
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break 
    
#cap.release()
#cv2.destroyAllWindows()
