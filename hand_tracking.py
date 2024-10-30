
import cv2
import time
import mediapipe as mp

cap =cv2.VideoCapture(0)


mpHand = mp.solutions.hands

hands = mpHand.Hands()

# max_num_hands = 2 -> default
# static_image_mode-> false-> detect, true-> detect
# max_num_hands = toplam takip edilecek el sayısı
# min_detection_confidence, min_tracking_confidence

mpDraw = mp.solutions.drawing_utils # mediapipe'ın drawing özelliklerini kullanıyoruz.
pTime = 0
cTime = 0


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results  = hands.process(imgRGB)
    print(results.multi_hand_landmarks)    
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,handLms,mpHand.HAND_CONNECTIONS)
        
            for id, lm in enumerate(handLms.landmark):
                print(id,lm)
                h, w, c = img.shape # h->height, w->weight, c->color
                
                # eklem bölgelerinin bilgilerini koordinatlara çevirelim.
                cx, cy = int(lm.x*w), int(lm.y*h)
                
                # Örneğin bileği görselleştirelim. 
                if id == 12:
                    cv2.circle(img, (cx,cy), 5, (255,0,0),cv2.FILLED) 
                    # imgtaki koordinatları cx,xy olan bölgeleri 5 boyda içi dolu mavi ile görselleştir.
                    
    
    # fps hesaplayalım.
    cTime = time.time()
    fps = 1 / (cTime-pTime)
    ptime = cTime
    
    # cv2.putText(img, "FPS: " + str(int(fps)), (10,75),cv2.FONT_HERSHEY_PLAIN,3,color=(255,0,0),thickness=5)
                
    
    cv2.imshow("img",img)
    cv2.waitKey(1)


cap.release()
cv2.destroyAllWindows()
