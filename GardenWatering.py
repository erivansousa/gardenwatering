from src.GPIOController import GPIOController
from src.DB import Database
from src.Models import Valve
import threading
import schedule
import time
import requests

gpioController = GPIOController()
database = Database()
valve = Valve()
md5Hash = ""

def changeMd5Hash(value):
	global md5Hash
	md5Hash = value

def configServerCheck():
	print("check server...")
	response = requests.get('https://weddingticketmanager.herokuapp.com/tmpGardenConfig', params={'hash': md5Hash})

	if(response.status_code == 200):
		print("found config change, updating local changes..")
		body = response.json()
		newHash = response.headers['md5Hash']

		db = database.getConfigDB()
		db.update({"type": "config"}, {"md5Hash": newHash, "value": body})

		changeMd5Hash(newHash)

		#config valve controll schedule
		configSchedule(body)

schedule.every(10).seconds.do(configServerCheck).tag('configChecker')

def configSchedule(conf):	
	schedule.clear('valve-control')
	settings = conf["settings"]

	#set irrigation duration
	valve.time_to_turnof = int(conf["duration"])

	if(conf['scheduleType'] == "INTERVAL"):		
		each = int(settings["each"])		
		if(settings["period"] == "HOUR"):
			#interval hour task
			schedule.every(each).hours.do(valve.turnValveOn).tag('valve-control')
		elif(settings["period"] == "MINUTE"):
			#interval minute task
			schedule.every(each).minutes.do(valve.turnValveOn).tag('valve-control')
		else:
			#interval undefined task (fallback 24 hour interval)
			schedule.every(24).hours.do(valve.turnValveOn).tag('valve-control')
	elif(conf['scheduleType'] == "DAILY"):
		#daily task
		hour = settings["time"]
		schedule.every().day.at(hour).do(valve.turnValveOn).tag('valve-control')
	else:
		#undefined period (fallback 24 hour interval)
		schedule.every(24).hours.do(valve.turnValveOn).tag('valve-control')

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

def main():
	#prepare and start valve controll schedule
	threading.Thread(target=valveControlThread, args=()).start()
		
	#get valve behavior from database
	data = database.getConfigDB()
	conf = data.getBy({"type": "config"})[0]

	changeMd5Hash(conf["md5Hash"])

	#config valve controll schedule
	configSchedule(conf['value'])
	
	while True:
		schedule.run_pending()
		time.sleep(1)

#=============================================================================
	#obter config do banco de dados
	#caso seja uma mudança nova, inicializa o scheduler
	#chama o servidor, caso o servidor atualize a config atualiza o registro no banco de dados e chama o fluxo para atualizar o schedule 
	#o scheduler aciona a valvula e aguarda o tempo de desligamento

if __name__ == "__main__":
	main()