# tests/roboflow/WebcamAccess.py

# Imports
import cv2

# Main
camera = cv2.VideoCapture("IP:PORT/video")

while True:
    isTrue, frame = camera.read()
    cv2.imshow('IP Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(1)
cv2.destroyAllWindows()
