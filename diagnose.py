import cv2
import os

def diagnose():
    print("Starting diagnostics...")
    
    # Check OpenCV
    try:
        print(f"OpenCV Version: {cv2.__version__}")
    except Exception as e:
        print(f"Error importing cv2: {e}")
        return

    # Check Haarcascade
    path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    if os.path.exists(path):
        print(f"Haarcascade file found at: {path}")
    else:
        print(f"Haarcascade file NOT found at: {path}")

    try:
        detector = cv2.CascadeClassifier(path)
        if detector.empty():
            print("Error: CascadeClassifier loaded but is empty.")
        else:
            print("CascadeClassifier loaded successfully.")
    except Exception as e:
        print(f"Error loading CascadeClassifier: {e}")

    # Check Camera
    try:
        print("Attempting to open camera (index 0)...")
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not open camera.")
        else:
            print("Camera opened successfully.")
            ret, frame = cap.read()
            if ret:
                print(f"Successfully captured a frame. Shape: {frame.shape}")
            else:
                print("Error: Could not read frame from camera.")
            cap.release()
    except Exception as e:
        print(f"Error accessing camera: {e}")

    print("Diagnostics complete.")

if __name__ == "__main__":
    diagnose()
