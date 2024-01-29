import board
import digitalio
import adafruit_rfm9x
from time import sleep

RADIO_FREQ_MHZ = 928.0
CS = digitalio.DigitalInOut(board.RFM_CS)
RESET = digitalio.DigitalInOut(board.RFM_RST)
rfm95 = adafruit_rfm9x.RFM9x(board.SPI(), CS, RESET, RADIO_FREQ_MHZ)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    packet = rfm95.receive()
    if packet is not None:
        led.value = True
        packet_text = str(packet, 'ascii')
        print(packet_text)
    else:
        led.value = False
        print("No signal.")
