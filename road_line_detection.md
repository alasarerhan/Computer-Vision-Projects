# Road Line Detection Project

## Description

This project implements a road line detection system using OpenCV. It processes video frames to detect and highlight lane markings on the road. The application uses techniques like color conversion, edge detection, and Hough Transform to identify lines in the specified region of interest.

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
   pip install opencv-python numpy
   ```

## How to Run

1. Place a video file of road footage in the appropriate directory.

2. Run the script:

   ```sh
   python road_line_detection.py
   ```

## Notes

- The script opens a window displaying the processed video with detected road lines.
- The region of interest is automatically defined, focusing on the area where lane markings are typically found.
- Press 'q' to quit the video window.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
