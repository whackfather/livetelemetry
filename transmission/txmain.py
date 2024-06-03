# Radio Trasmitter Program
# v1.13
# Written by Roman Rodriguez

import board
import busio
import analogio
import digitalio
import adafruit_rfm9x
import adafruit_ms8607
import time

RADIO_FREQ_MHZ = 928.0
CS = digitalio.DigitalInOut(board.RFM_CS)
RESET = digitalio.DigitalInOut(board.RFM_RST)
rfm95 = adafruit_rfm9x.RFM9x(board.SPI(), CS, RESET, RADIO_FREQ_MHZ)
rfm95.tx_power = 23
i2c = board.I2C()
traw = analogio.AnalogIn(board.A0)
ms = adafruit_ms8607.MS8607(i2c)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

tank = str(traw.value)
pres = str(ms.pressure)
start = time.monotonic()
rfm95.send(tank + "," + pres + ",0")

while True:
    tank = str(traw.value)
    pres = str(ms.pressure)
    end = time.monotonic()
    elapsed = end - start
    start = time.monotonic()
    led.value = True
    rfm95.send(tank + "," + pres + "," + str(elapsed))
    led.value = False
