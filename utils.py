import cv2

def draw_faces(frame, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return frame

def draw_fps(frame, fps):
    cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return frame

def draw_face_count(frame, count):
    cv2.putText(frame, f"Faces: {count}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return frame

def resize_frame(frame, width=640):
    height, original_width = frame.shape[:2]
    if original_width > width:
        ratio = width / original_width
        new_height = int(height * ratio)
        return cv2.resize(frame, (width, new_height))
    return frame
