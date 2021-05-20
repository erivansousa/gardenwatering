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
		gpio.output(VALVE_PIN, gpio.HIGH)

	def closeValve(self):
		gpio.output(VALVE_PIN, gpio.LOW)

	def getTime(self):
		bus = SMBus(rpiChannel)
		bus.read_i2c_data(CLK_I2C_ADDRESS, 0)
		return 12342345245



	def __del__(self):
		gpio.cleanup()
