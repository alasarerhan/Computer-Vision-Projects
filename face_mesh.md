# Face Mesh Project

## Description

This project uses MediaPipe and OpenCV to detect faces and perform face meshing on a video. The application reads a video file, detects faces in each frame, and applies face meshing to identify key regions of interest (eyes, eyebrows, nose, lips, etc.).

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

1. Ensure your video file is located at `your_file_path`.

2. Run the script:

   ```sh
   python face_mesh.py
   ```

## Notes

- Press 'q' to quit the video window.
- Adjust the face meshing parameters as needed.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

