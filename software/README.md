# Software

Onboard computer: Raspberry Pi 5 (8 GB)  
Camera: Raspberry Pi Camera Module 3

## Folders
- `camera/` — Picamera2 RGB capture
- `detection/` — YOLOv8n sample + class list
- `gps/` — Neo-6M UART coordinates
- `motors/` — GPIO on/off demo for driver pins
- `servo_pca9685/` — MG996R sweep on PCA9685

## Level 2 work
1. Run camera + YOLOv8n on a sign/cone
2. Stop on ultrasonic threshold
3. Drive motors through BTS7960 / Cytron
4. Read GPS lat/long
5. Move one steering / gripper servo
