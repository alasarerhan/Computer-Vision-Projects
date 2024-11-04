# Face Detection Project

## Description

This project uses MediaPipe and OpenCV to detect faces in a video. The application reads a video file, processes each frame to detect faces, and draws bounding boxes around the detected faces.

## Setup

1. **Clone the repository**

   ```sh
   git clone https://github.com/alasarerhan/face-detection-project.git
   cd face-detection-project
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

1. Ensure your video file is located at `your_file_path`.

2. Run the script:

   ```sh
   python face_detection.py
   ```

## Notes

- Press 'q' to quit the video window.
- Adjust the face detection confidence threshold as needed. The current value is set to 0.2.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
