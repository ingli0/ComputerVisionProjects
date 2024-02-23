# HandControl Project
 

## Overview

Hand holder has inside Python project that utilizes computer vision to interact with your computer using hand gestures. The project consists of three main components:

1.**mouseVirtual.py**: Enables users to control the mouse cursor using hand movements.
![image](https://github.com/ingli0/ComputerVisionProjects/assets/76855285/79ab956c-d928-48a3-a3aa-0d3a0f781b9a)

**Guide**
index up:
you use the mouse via camera 

index and middle up:
it press left click

index and middle and ring up:
it press double left click 

thumb and pinkie :
it scrolls up 

fist:
it scrolls down 
  
  
2. **fingerCount.py**: Determines the number of raised fingers using computer vision.
![image](https://github.com/ingli0/ComputerVisionProjects/assets/76855285/40c80a8a-33f8-4a6e-bfdd-46b193dd02d6)

3. **volumeHandcontrol.py**: Allows users to control system volume using hand gestures.
![image](https://github.com/ingli0/ComputerVisionProjects/assets/76855285/f64a5c25-e28d-4b92-a103-8fa6f1d844c5)

 



## Features

- **Finger Counting:** The `fingerCount` module utilizes computer vision to count the number of fingers raised.

- **Volume Control:** With `volumeHandcontrol.py`, users can adjust the system volume by making specific hand gestures.

- **Virtual Mouse:** The `mouseVirtual.py` module allows users to control the mouse cursor by moving their hand.

## Prerequisites

Ensure you have the following dependencies installed:

- Python 3.8
- OpenCV
- mediapipe
- autopy
- comtypes
- pycaw
- pyautogui

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ingli0/ComputerVisionProjects.git

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt 

3. **Run the desired module:**
   ```bash
   fingerCount.py
   mouseVirtual.py
   VolumeHandControl.py
