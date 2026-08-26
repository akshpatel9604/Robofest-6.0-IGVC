from gpiozero import DigitalOutputDevice
from time import sleep

out = DigitalOutputDevice(16)  # output pin

try:
    while True:
        out.on()      # HIGH
        sleep(2)
        out.off()     # LOW
        sleep(2)
except KeyboardInterrupt:
    out.close()
