class Valve:
	def __init__(self):
		self.is_valve_on = False
		self.time_to_turnof = 2
	
	def valveState(self): return self.is_valve_on
	def turnValveOn(self): self.is_valve_on = True
	def turnValveOff(self): self.is_valve_on = False
	def getOpenedTime(self): self.time_to_turnof
	def setOpenedTime(self, openedTime): self.time_to_turnof = openedTime