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

while True:
    start = time.monotonic()
    packet = rfm95.receive()
    if packet is not None:
        led.value = True
        packet_text = str(packet, 'ascii')
        print(packet_text)
    else:
        led.value = False
        ls_packet = list(packet_text.split(","))
        end = time.monotonic()
        elapsed = end - start
        ls_packet[4] = elapsed
        print(str(ls_packet).replace("[", "").replace("'", "").replace(" ", "").replace("]", ""))
