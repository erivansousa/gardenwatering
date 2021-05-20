from pysondb import db

class Database:
	def __init__(self):
		self.configdb = db.getDb('..\db\garden_cfg.json')
		
	def getConfigDB(self):
		return self.configdb
