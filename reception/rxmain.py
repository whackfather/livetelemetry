# Radio Receiver Program
# v1.14
# Written by Roman Rodriguez

import board
import digitalio
import adafruit_rfm9x
import time

RADIO_FREQ_MHZ = 928.0
CS = digitalio.DigitalInOut(board.RFM_CS)
RESET = digitalio.DigitalInOut(board.RFM_RST)
rfm95 = adafruit_rfm9x.RFM9x(board.SPI(), CS, RESET, RADIO_FREQ_MHZ)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
packet_text = "0,0,0,0,0"
lost = 0

while True:
    packet = rfm95.receive()
    if packet is not None:
        if lost == 1:
            lost = False
            led.value = True
            packet_text = str(packet, 'ascii')
            ls_packet = list(packet_text.split(","))
            end = time.monotonic()
            elapsed = end - start
            ls_packet[4] = elapsed
            print(str(ls_packet).replace("[", "").replace("'", "").replace(" ", "").replace("]", ""))
        elif lost == 0:
            led.value = True
            packet_text = str(packet, 'ascii')
            print(packet_text)
    else:
        led.value = False
        if lost == 0:
            lost = 1
            start = time.monotonic()
