# Gripper — Level 3 plan

The chassis in `cad/chassis` is the Level 1 mechanical baseline.
This folder is for the gripper that will be used in later IGVC stages
(object pickup and parking alignment).

## Planned hardware
- 2-finger or scoop gripper
- Actuation: MG996R servo on PCA9685
- Mount: 3D-printed bracket on the front aluminium extrusion
- Optional: small ultrasonic or camera view for grasp alignment

## Files to be placed here
- gripper CAD / Blender screenshots
- servo horn and linkage drawing
- mount dimensions

## Control
- Raspberry Pi 5 → I2C → PCA9685 → gripper servo
- Open / close angles will be tuned on the real rover
