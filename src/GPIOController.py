import RPi.GPIO as gpio

VALVE_PIN = 17

class GPIOController:

	def __init__(self):
		gpio.setmode(gpio.BCM)
		gpio.setwarnings(False)
		gpio.setup(VALVE_PIN, gpio.OUT)


	def openValve(self):
		gpio.output(VALVE_PIN, gpio.HIGH)

	def closeValve(self):
		gpio.output(VALVE_PIN, gpio.LOW)



	def __del__(self):
		gpio.cleanup()
