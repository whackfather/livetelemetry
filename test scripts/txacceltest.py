import board
import busio
import digitalio
import adafruit_rfm9x
import adafruit_bno055
import time

RADIO_FREQ_MHZ = 928.0
CS = digitalio.DigitalInOut(board.RFM_CS)
RESET = digitalio.DigitalInOut(board.RFM_RST)
rfm95 = adafruit_rfm9x.RFM9x(board.SPI(), CS, RESET, RADIO_FREQ_MHZ)
i2c = board.I2C()
bno = adafruit_bno055.BNO055_I2C(i2c)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

accel = bno.linear_acceleration
accel = str(accel)
start = time.monotonic()
rfm95.send(accel.replace(" ", "").replace("(", "").replace(")", "") + ",0")

while True:
    accel = bno.linear_acceleration
    accel = str(accel)
    euler = bno.euler
    end = time.monotonic()
    elapsed = end - start
    start = time.monotonic()
    led.value = True
    rfm95.send(accel.replace(" ", "").replace("(", "").replace(")", "") + "," + str(elapsed))
    led.value = False
