# Virtual Keyboard Project

## Overview:
This project implements a virtual keyboard system using computer vision techniques. It allows users to interact with their computers without physically touching the keyboard. The system detects hand gestures using a webcam, interprets them, and simulates key presses accordingly.

## Features:
- **Hand Gesture Recognition**: Utilizes the MediaPipe library to detect and track hand landmarks in real-time.
- **Virtual Keyboard Interface**: Displays a graphical representation of the keyboard on the screen.
- **Key Press Simulation**: Simulates key presses when a hand gesture is recognized over a key on the virtual keyboard.
- **Typed Word Display**: Displays the word being typed on the virtual keyboard in real-time on the screen.

## Dependencies:
- OpenCV: For capturing and processing webcam frames.
- MediaPipe: For hand landmark detection and tracking.
- pynput: For simulating key presses.
- Python: Programming language used for implementation.

## Usage:
1. Run the Python script `virtual_keyboard.py`.
2. Position your hand in front of the webcam.
3. Move your hand over the virtual keys to type characters.
4. The typed word will be displayed in real-time on the screen.

## Future Enhancements:
- Improve hand gesture recognition accuracy.
- Implement support for additional languages and characters.
- Add voice input functionality.
- Enhance the user interface with more customization options.


