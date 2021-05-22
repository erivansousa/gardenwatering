from src.GPIOController import GPIOController
from src.DB import Database
import threading
import schedule
import time

class Valve:
	def __init__(self):
		self.is_valve_on = False
		self.time_to_turnof = 2
	
	def valveState(self): return self.is_valve_on
	def turnValveOn(self): self.is_valve_on = True
	def turnValveOff(self): self.is_valve_on = False
	def getOpenedTime(self): self.time_to_turnof
	def setOpenedTime(self, openedTime): self.time_to_turnof = openedTime

gpioController = GPIOController()
database = Database()
valve = Valve()


def configServerCheck():
	print("check server...")

def configSchedule(conf):	
	schedule.clear('valve-control')
	schedule.every(10).seconds.do(valve.turnValveOn).tag('valve-control')
	#reconfigure shcedule based on the conf

def valveControlThread():
	print("valve controll started")
	while True:
		if valve.valveState():
			gpioController.openValve()
			print("Valve opened")
			time.sleep(valve.time_to_turnof)
			gpioController.closeValve()
			print("Valve closed")
			valve.turnValveOff()

schedule.every(10).seconds.do(configServerCheck).tag('configChecker')
schedule.every(10).seconds.do(valve.turnValveOn).tag('valve-control')

def main():
	print("Hello Garden")

	#prepare and start valve controll schedule
	threading.Thread(target=valveControlThread, args=()).start()
		
	#get valve behavior from database
	data = database.getConfigDB()
	conf = data.getBy({"type": "config"})[0]

	#config valve controll schedule
	configSchedule(conf)
	
	while True:
		schedule.run_pending()
		time.sleep(1)

	#obter config do banco de dados
	#caso seja uma mudança nova, inicializa o scheduler
	#chama o servidor, caso o servidor atualize a config atualiza o registro no banco de dados e chama o fluxo para atualizar o schedule 
	#o scheduler aciona a valvula e aguarda o tempo de desligamento
	
	#while (True):
	#	gpioController.openValve()
	#	time.sleep(2)
	#	gpioController.closeValve()
	#	time.sleep(2)

	#data.add({'type': 'breakFlag', 'value': 'False'})
	#print(data.getAll())	

		#lastConfigCheck = checkConfigServer(lastConfigCheck)
		#breakConfig = data.getBy({'type': 'breakFlag'})[0]
		#breakFlag = bool(breakConfig['value'])		
		
		#if breakFlag:
		#	break

if __name__ == "__main__":
	main()