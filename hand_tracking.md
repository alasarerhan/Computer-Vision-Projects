# Hand Tracking Application

This application is a Python program that tracks and visualizes hand movements in real-time. It uses MediaPipe and OpenCV libraries to detect and mark hand movements through the webcam.

## Features

- Real-time hand tracking
- Visualization of hand joints
- FPS (Frames Per Second) indicator
- Special joint point highlighting (blue marking for joint number 12)

## Requirements

```
opencv-python
mediapipe
```

## Installation

1. Install required libraries:
```bash
pip install opencv-python mediapipe
```

2. Run the program:
```bash
python hand_tracking.py
```

## Code Explanation

### Core Components

1. **Video Capture**
   - Video is captured from webcam using `cv2.VideoCapture(0)`
   - Parameter 0 represents the default camera

2. **MediaPipe Hand Tracking Module**
   - Hand tracking feature is initiated with `mp.solutions.hands`
   - Hand tracking object is created with `hands = mpHand.Hands()`
   - Default settings:
     - max_num_hands = 2 (maximum number of hands to track)
     - static_image_mode = False (continuous tracking mode)

3. **Visualization**
   - Hand landmarks are drawn using `mp.solutions.drawing_utils`
   - FPS is calculated and displayed
   - Joint point number 12 is specially marked

### Main Loop Function

```python
while True:
    # Capture image
    success, img = cap.read()
    
    # Convert BGR to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Hand detection
    results = hands.process(imgRGB)
    
    # Process and visualize detected hands
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # Draw hand landmarks
            mpDraw.draw_landmarks(img, handLms, mpHand.HAND_CONNECTIONS)
```

## Usage

1. When the program is run, webcam view opens
2. Place your hand in the camera's field of view
3. The program will automatically track and mark your hand movements
4. Press 'q' to exit

## Hand Landmark Points

MediaPipe hand tracking system detects 21 different points (landmarks) for each hand:
- 0-4: Thumb points
- 5-8: Index finger points
- 9-12: Middle finger points
- 13-16: Ring finger points
- 17-20: Pinky finger points

## Troubleshooting

1. Camera Access Error:
   - Make sure the camera is connected
   - Ensure no other application is using the camera

2. Low FPS:
   - Check your computer's processing power
   - Close applications running in the background

## How to Contribute

1. Fork this repository
2. Create a new branch
3. Commit your changes
4. Push your branch
5. Create a pull request

## Code Breakdown

### Initialization
```python
import cv2
import time
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpHand = mp.solutions.hands
hands = mpHand.Hands()
mpDraw = mp.solutions.drawing_utils
```

### Frame Processing
- The program continuously captures frames from the webcam
- Each frame is converted from BGR to RGB color space
- MediaPipe processes the RGB image to detect hands
- Detected hand landmarks are drawn on the original image

### Performance Monitoring
```python
cTime = time.time()
fps = 1 / (cTime-pTime)
pTime = cTime
```
- FPS calculation helps monitor the application's performance
- The value is displayed in real-time on the video feed

## Advanced Features

### Custom Point Detection
- The program specifically highlights joint point 12
- This can be modified to track different points or multiple points
- Color and size of the markers can be customized

### Hand Tracking Parameters
You can modify the hand tracking parameters:
```python
hands = mpHand.Hands(
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
```

## License

This project is licensed under the MIT License.
