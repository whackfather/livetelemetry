# Altitude from Air Pressure
# v0.1
# Roman Rodriguez

import math

pres = float(input("Test pressure: "))

def altitude(x):
	if x >= 22632.11:
		alt = (288/-0.0065) * ((x / 101325) ** ((-8.31432 * -0.0065)/(9.80665 * 0.0289644)) - 1)
		return alt
	elif x < 22632.11:
		alt = 11000 + ((8.31432 * 216.5 * math.log(x / 22632.11)) / (-9.80665 * 0.0289644))
		return alt


print(altitude(pres))
