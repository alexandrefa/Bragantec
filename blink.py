import mraa
import time

led = mraa.Gpio(23)
led.dir(mraa.DIR_OUT)

while True:

	led.write(1)
	time.sleep(0.2)
	led.write(0)
	time.sleep(0.2)
