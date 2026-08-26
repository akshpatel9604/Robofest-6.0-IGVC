from adafruit_servokit import ServoKit
import time

pca = ServoKit(channels=16)

pca.servo[0].angle = 0

for i in range(100):
    pca.servo[0].angle = i
    time.sleep(0.1)

for i in range(180, 0, -1):
    pca.servo[0].angle = i
    time.sleep(0.1)
