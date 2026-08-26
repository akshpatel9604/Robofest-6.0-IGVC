from ultralytics import YOLO
from picamera2 import Picamera2
import cv2

model = YOLO("yolov8n.pt")

cam = Picamera2()
cam.configure(cam.create_preview_configuration(main={"size": (640, 480)}))
cam.start()

while True:
    frame = cam.capture_array()
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    results = model(frame, verbose=False)
    plotted = results[0].plot()

    cv2.imshow("YOLOv8n", plotted)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cam.stop()
cv2.destroyAllWindows()
