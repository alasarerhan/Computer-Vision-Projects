import cv2
import numpy as np

def region_of_interest(image, vertices):
    mask = np.zeros_like(image)
    
    match_mask_color = 255
    
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def drawLines(image, lines):
    if lines is None:  # If lines are None, stop the process.
        return image

    for line in lines:
        x1, y1, x2, y2 = line[0]  # Get the coordinates of each line.
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 3)  # Draw the line.
    return image  # Return the image with the drawn lines.

def process(image):
    height, width = img.shape[0], img.shape[1]
    
    region_of_interest_vertices = [(0, height), (width/2, height/2), (width, height)]
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    canny_image = cv2.Canny(gray_image, 150, 50)
    cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))
    lines = cv2.HoughLinesP(cropped_image, rho=2, theta=np.pi/180, threshold=250, lines=np.array([]), minLineLength=200, maxLineGap=5)
    # print(lines)
    imageWithLine = drawLines(image, lines)
    return imageWithLine

cap = cv2.VideoCapture("3_Goruntu isleme Projeleri/8_road_line_detection/video1.mp4") 

while True:
    success, img = cap.read()
    img = process(img)
    if success:
        cv2.imshow("img", img)
        cv2.waitKey(20)
    else: 
        break
     
cap.release()
cv2.destroyAllWindows()
