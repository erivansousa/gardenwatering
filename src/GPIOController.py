import RPi.GPIO as gpio
from smbus2 import SMBus

VALVE_PIN = 17

rpiChannel = 1

CLK_I2C_ADDRESS = 0x68

class GPIOController:

	def __init__(self):
		gpio.setmode(gpio.BCM)
		gpio.setwarnings(False)
		gpio.setup(VALVE_PIN, gpio.OUT)

	def openValve(self):
		gpio.output(VALVE_PIN, gpio.LOW)

	def closeValve(self):
		gpio.output(VALVE_PIN, gpio.HIGH)

	def getTime(self):
		bus = SMBus(rpiChannel)
		data = bus.read_byte(CLK_I2C_ADDRESS, 0)
		return data



	def __del__(self):
		gpio.cleanup()
