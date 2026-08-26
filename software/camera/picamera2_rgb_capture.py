from picamera2 import Picamera2
import cv2

cam = Picamera2()
config = cam.create_preview_configuration(
    main={"size": (640, 480), "format": "RGB888"}
)
cam.configure(config)
cam.start()

while True:
    frame = cam.capture_array()
    color_img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.imshow("RGB image", color_img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cam.stop()
cv2.destroyAllWindows()
