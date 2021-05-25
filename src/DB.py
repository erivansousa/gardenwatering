from pysondb import db

class Database:
	def __init__(self):
		self.configdbFile = '..\db\garden_cfg.json'
		
	def getConfigDB(self):
		return db.getDb(self.configdbFile)
