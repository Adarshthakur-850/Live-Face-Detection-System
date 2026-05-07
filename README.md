# Live Face Detection System

A production-quality, real-time face detection system using Python and OpenCV.

## Features
- **Real-time Detection**: Uses Haar Cascades for fast face detection.
- **Threaded Video Capture**: Ensures smooth video playback without blocking the detection loop.
- **Performance Optimized**: Resizes frames for faster processing.
- **FPS Display**: Shows frames per second and detected face count.

## Project Structure
```
face_detection/
│
├── main.py          # Entry point
├── detector.py      # Face detection logic
├── camera.py        # Threaded camera capture class
├── utils.py         # Helper functions for drawing and display
└── requirements.txt # Project dependencies
```

## Requirements
- Python 3.x
- Webcam

## Installation

1.  **Clone or Download** this repository.
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the application**:
    ```bash
    python main.py
    ```
2.  **Exit**:
    Press `q` to quit the application.

## Docker Usage

This project includes a `Dockerfile` for running the application in a container.

### 1. Build the Image
```bash
docker build -t face-detection-app .
```

### 2. Run the Container
Running GUI applications and accessing the webcam from Docker requires specific flags depending on your OS.

#### Linux
```bash
docker run -it --rm --device=/dev/video0 -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix face-detection-app
```
*Note: You may need to run `xhost +local:docker` on your host machine to allow the container to access the display.*

#### Windows
Running GUI/Webcam apps from Docker Desktop on Windows is complex and requires:
1.  **X Server**: Install VcXsrv (or Xming) to handle the GUI.
2.  **WSL2**: Ensure you are using the WSL2 backend.
3.  **Command**:
    ```powershell
    # Assuming VcXsrv is running correctly with "Disable access control" checked
    docker run -it --rm -e DISPLAY=host.docker.internal:0.0 face-detection-app
    ```
*Note: Webcam passthrough to Docker on Windows is experimental and may require specific kernel drivers or third-party tools (like USBIP).*

## Troubleshooting
- If the camera doesn't open, ensure no other application is using it.
- If faces are not detected, ensure good lighting and face the camera directly.
- **Docker**: If you encounter "cannot open display" errors, verify your X Server settings (X11 forwarding).
