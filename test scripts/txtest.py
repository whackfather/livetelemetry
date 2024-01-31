import board
import digitalio
import adafruit_rfm9x
from time import sleep
from adafruit_ms8607 import MS8607

RADIO_FREQ_MHZ = 915.0
CS = digitalio.DigitalInOut(board.RFM_CS)
RESET = digitalio.DigitalInOut(board.RFM_RST)
rfm95 = adafruit_rfm9x.RFM9x(board.SPI(), CS, RESET, RADIO_FREQ_MHZ)
i2c = board.I2C()
sensor = MS8607(i2c)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    pres = sensor.temperature
    rfm95.send(str(pres))
