import cv2
import numpy as np

def test_gui():
    print("Testing cv2.imshow...")
    img = np.zeros((200, 200, 3), dtype='uint8')
    cv2.imshow("Test Window", img)
    print("Window created. Press any key to close (or wait 2s).")
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
    print("Test complete.")

if __name__ == "__main__":
    try:
        test_gui()
    except Exception as e:
        print(f"Error during GUI test: {e}")
