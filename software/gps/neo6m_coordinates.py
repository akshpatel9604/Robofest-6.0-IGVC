import serial
import pynmea2

port = "/dev/serial0"
s = serial.Serial(port, baudrate=9600, timeout=0.8)

while True:
    data = s.readline().decode("utf-8", errors="ignore")
    if data.startswith("$GPGLL") or data.startswith("$GNGLL"):
        location = pynmea2.parse(data)
        latitude = location.latitude
        longitude = location.longitude
        print("Latitude:", latitude, "\tLongitude:", longitude)
