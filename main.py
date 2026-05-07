import cv2
import time
from camera import WebcamStream
from detector import FaceDetector
import utils

def main():
    vs = WebcamStream(src=0).start()
    detector = FaceDetector()
    time.sleep(2.0)

    fps_start_time = time.time()
    fps_counter = 0
    fps = 0

    try:
        while True:
            frame = vs.read()
            if frame is None:
                break
            
            frame = utils.resize_frame(frame, width=800)
            faces = detector.detect(frame)
            
            frame = utils.draw_faces(frame, faces)
            frame = utils.draw_fps(frame, fps)
            frame = utils.draw_face_count(frame, len(faces))

            cv2.imshow("Live Face Detection", frame)

            fps_counter += 1
            if (time.time() - fps_start_time) > 1:
                fps = fps_counter / (time.time() - fps_start_time)
                fps_counter = 0
                fps_start_time = time.time()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        print("Interrupted by user")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        vs.stop()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
