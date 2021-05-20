from src.GPIOController import GPIOController
from src.DB import Database
import datetime
import json

gpioController = GPIOController()
database = Database()

def main():
	print("Hello Garden")
	lastConfigCheck = 0
	
	#db = TinyDB('db/gardem_cfg.json')
	#db.insert({'id': '345abf', 'value': 'value de teste'})
	#print(db.all())
	
	#while (True):
	#	gpioController.openValve()
	#	time.sleep(2)
	#	gpioController.closeValve()
	#	time.sleep(2)

	data = database.getConfigDB()
	#data.add({'type': 'breakFlag', 'value': 'False'})
	#print(data.getAll())
	
	while True:
		lastConfigCheck = checkConfigServer(lastConfigCheck)
		#breakConfig = data.getBy({'type': 'breakFlag'})[0]
		#breakFlag = bool(breakConfig['value'])		
		
		#if breakFlag:
		#	break



def checkConfigServer(last):
	now = datetime.datetime.now()
	if(now - last >= 60):
		print('checking...')
		return now


if __name__ == "__main__":
	main()
