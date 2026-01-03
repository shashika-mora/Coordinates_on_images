# Coordinates on Images

![Python](https://img.shields.io/badge/python-3.x-blue?style=flat-square&logo=python&logoColor=white) ![OpenCV](https://img.shields.io/badge/opencv-python-green?style=flat-square&logo=opencv&logoColor=white)

## Overview
This project provides a simple OpenCV-based tool to inspect images. It allows users to interactively view the coordinates of pixels and their corresponding BGR color values by clicking on an image.

- **Left Mouse Button**: Displays the (x, y) coordinates of the clicked point.
- **Right Mouse Button**: Displays the BGR (Blue, Green, Red) color values of the clicked pixel.

## Installation

Ensure you have Python installed. Then, install the required dependencies:

```bash
# Clone the repository (if applicable)
# git clone [repository-url]

# Install OpenCV
pip install opencv-python
```

## Usage

1.  Place your target image in the project directory (default expected filename is `image.png` or modify `main.py` to point to your image).
2.  Run the application:

```bash
python main.py
```

3.  Interact with the opened window:
    -   Click **Left Button** to see coordinates.
    -   Click **Right Button** to see RGB values.
    -   Press any key to close the window.

## Structure
-   `main.py`: The main script that runs the image viewer and handles mouse events.
-   `mouse_events.py`: A utility script to list all available mouse events in OpenCV.
-   `image.png`: (Required) The input image file to be analyzed.

---

*Created by AMST DAYARATHNA*