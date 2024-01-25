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

pres = ms.pressure
temp = ms.temperature
acx = adxl.raw_x
acy = adxl.raw_y
acz = adxl.raw_z
start = time.monotonic()
rfm95.send(str(pres) + "," + str(temp) + "," + str(acx) + "," + str(acy) + "," + str(acz))

while True:
	pres = ms.pressure
	temp = ms.temperature
	acx = adxl.raw_x
	acy = adxl.raw_y
	acz = adxl.raw_z
	end = time.monotonic()
	elapsed = end - start
	start = time.monotonic()
	led.value = True
	rfm95.send(str(pres) + "," + str(temp) + "," + str(acx) + "," + str(acy) + "," + str(acz) + "," + str(elapsed))
	led.value = False
