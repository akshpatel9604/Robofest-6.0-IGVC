# Robofest-6.0-IGVC
**Team Cognitrek**, Dharmsinh Desai University  
Robofest Gujarat 6.0 — Senior — Intelligent Ground Vehicle Competition

## Overview
6-wheel autonomous rover for outdoor IGVC tasks: navigation, obstacles,
ramp/tunnel, QR/AprilTag, traffic signs, grasping and parking.

## Stack
- Compute: Raspberry Pi 5 (8 GB)
- Vision: Camera Module 3 + YOLOv8n
- Distance: ultrasonic sensors
- Drive: 6 DC motors + BTS7960 / Cytron
- Steering / gripper: MG996R + PCA9685
- GPS: Neo-6M
- Power: 12V 30Ah lithium + 5V buck for Pi 5

## Repository
- `cad/` — chassis views and gripper plan
- `docs/` — ideation PDF, notes, component list
- `electronics/` — control diagram and PCB schematic
- `images/` — rover renders
- `software/` — Pi 5 sample codes
- `references/` — sources

Ideation PDF: `docs/IGVC IDEATION ROBOFEST 6.0 PDF.pdf`
