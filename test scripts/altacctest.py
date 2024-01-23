import time
import board
import digitalio
import adafruit_adxl34x

i2c = board.I2C()
accelerometer = adafruit_adxl34x.ADXL345(i2c)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
	led.value = True
	acc = accelerometer.raw_x
	actual = (acc * 0.0039) * 9.80665
	print(actual)
	time.sleep(0.05)
	led.value = False
	time.sleep(0.05)
