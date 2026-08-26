# Neo-6M GPS

UART GPS code for Raspberry Pi 5.

## Wiring
- Neo-6M TX -> Pi 5 RX
- Neo-6M RX -> Pi 5 TX
- VCC -> 5V
- GND -> GND

## Run on Raspberry Pi 5
Enable Serial Port and disable Serial Console.
Then run:

python3 neo6m_coordinates.py
