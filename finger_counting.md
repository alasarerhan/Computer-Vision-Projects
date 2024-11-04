# Finger Counting Project

## Description

This project uses MediaPipe and OpenCV to track hand movements and count the number of fingers shown. The application captures video from a webcam, detects hands, and identifies the landmarks on the hands to determine which fingers are extended.

## Setup

1. **Clone the repository**

   ```sh
   git clone https://github.com/alasarerhan/computer-vision-projects.git
   cd computer-vision-projects
   ```

2. **Create a virtual environment**

   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**

   ```sh
   pip install opencv-python mediapipe
   ```

## How to Run

1. Ensure your webcam is connected.

2. Run the script:

   ```sh
   python finger_counting.py
   ```

## Notes

- The script will open a window displaying the webcam feed with hand tracking and finger counting.
- The number of fingers detected will be displayed on the screen.
- Press 'q' to quit the video window.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
