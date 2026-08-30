# Ideation Notes — Team Cognitrek
Dharmsinh Desai University
Robofest Gujarat 6.0 | Senior | IGVC

## Team
- Team name: Cognitrek
- Mentor: Prof. Gopal Gohel
- Members: (1) Patel Aksh (B.tech | ECE | 3rd year)
           (2) Patel Om  (B.tech | ECE | 3rd year)
           (3) Patel Aniruddh  (B.tech | ECE | 3rd year)
           (4) Donga Sanket  (B.tech | ECE | 3rd year)

## Aim
Build a 6-wheel autonomous ground rover that can complete Robofest 6.0 IGVC tasks:
basic navigation, obstacle avoidance, terrain crossing, QR/AprilTag route selection,
traffic-sign response, dynamic wait-and-go, object grasping and parking.

## Why Raspberry Pi 5
Official guidelines allow Raspberry Pi or Jetson Nano.
We selected Raspberry Pi 5 (8 GB) because:
- it is enough for the official tasks
- Camera Module 3 works natively
- cost fits a Level-1 budget better than Jetson Nano + RealSense
- GPIO, I2C and UART are enough for drivers, PCA9685 and GPS

## Sensing plan
- Camera Module 3: RGB vision for signs, QR/AprilTag, parking and grasp alignment
- Ultrasonic sensors: close-range distance for cones, boxes, tunnel and underpass
- Neo-6M GPS: optional coarse location
- Encoders / IMU: later, for parking and ramp stability

## Software plan
- OpenCV + Picamera2
- YOLOv8n / YOLO11n for contest objects
- OpenCV for QR / AprilTag
- gpiozero for GPIO
- Adafruit ServoKit for PCA9685
- pyserial + pynmea2 for GPS

## Mechanical plan
- 6-wheel drive
- balloon tyres 10–12 inch (280 mm)
- aluminium 20 x 20 mm chassis
- shocks for ramps and uneven ground
- size near 100 × 90 × 63 cm
- width kept under 4 ft passage / tunnel / underpass
- ground clearance about 120 mm

## Power plan
- 12V battery for motors
- 12V-to-5V buck for Raspberry Pi 5
- motors and Pi on separate rails, common ground
- hardware emergency stop
