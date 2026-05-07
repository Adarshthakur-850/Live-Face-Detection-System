# Live Face Detection System

A real-time **Live Face Detection System** built using **Python, OpenCV, and Machine Learning/Computer Vision techniques** to detect human faces through webcam input or uploaded images.

## Project Overview

This project captures live video from a webcam and detects human faces in real time. It can be used for:

* Face detection in live video streams
* Security and surveillance systems
* Attendance systems
* Smart camera applications
* Human-computer interaction projects

The system processes each video frame, identifies facial regions, and highlights detected faces using bounding boxes.

---

## Features

* Real-time face detection using webcam
* Detects multiple faces simultaneously
* Fast frame processing
* Bounding box visualization around faces
* Easy to run locally
* Lightweight implementation

---

## Tech Stack

* **Python**
* **OpenCV**
* **NumPy**
* Haar Cascade / Deep Learning Face Detection Model

---

## Project Structure

```bash
Live-Face-Detection-System/
│── app.py / main.py
│── face_detection.py
│── requirements.txt
│── haarcascade_frontalface_default.xml
│── model/
│── screenshots/
│── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Adarshthakur-850/Live-Face-Detection-System.git
cd Live-Face-Detection-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run

Run the application:

```bash
python app.py
```

OR

```bash
python main.py
```

The webcam will open and start detecting faces in real time.

Press **Q** to quit.

---

## Working Flow

1. Capture live webcam feed
2. Convert frames for processing
3. Apply face detection model
4. Detect facial regions
5. Draw bounding boxes
6. Display output in real-time

---

## Sample Output

Add screenshots or GIFs of your project here.

Example:

* Face detected in webcam stream
* Multiple face detection
* Real-time bounding box output

---

## Future Improvements

* Face recognition integration
* Emotion detection
* Mask detection
* Attendance automation
* Deployment using Flask/Streamlit
* Cloud integration

---

## Author

**Adarsh Thakur**

GitHub: [https://github.com/Adarshthakur-850](https://github.com/Adarshthakur-850)

---

## License

This project is open-source and available under the MIT License.
