import board
import digitalio
import adafruit_rfm9x
from adafruit_ms8607 import MS8607
import adafruit_adxl34x
import time

RADIO_FREQ_MHZ = 928.0
CS = digitalio.DigitalInOut(board.RFM_CS)
RESET = digitalio.DigitalInOut(board.RFM_RST)
rfm95 = adafruit_rfm9x.RFM9x(board.SPI(), CS, RESET, RADIO_FREQ_MHZ)
i2c = board.I2C()
ms = MS8607(i2c)
adxl = adafruit_adxl34x.ADXL345(i2c)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

accel = adxl.acceleration
accel = str(accel)
pres = ms.pressure
temp = ms.temperature
start = time.monotonic()
rfm95.send(str(pres) + "," + str(temp) + "," + accel.replace(" ", "").replace("(", "").replace(")", "") + ",0")

while True:
    accel = adxl.acceleration
    accel = str(accel)
    pres = ms.pressure
    temp = ms.temperature
    end = time.monotonic()
    elapsed = end - start
    start = time.monotonic()
    led.value = True
    rfm95.send(str(pres) + "," + str(temp) + "," + accel.replace(" ", "").replace("(", "").replace(")", "") + "," + str(elapsed))
    led.value = False
