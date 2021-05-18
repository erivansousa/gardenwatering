from tinydb import TinyDB, Query
from src.GPIOController import GPIOController
import time

gpioController = GPIOController()

def main():
	print("Hello Garden")
	while True:
		gpioController.openValve()
		time.sleep(2)
		gpioController.closeValve()
		time.sleep(1)


if __name__ == "__main__":
	main()
