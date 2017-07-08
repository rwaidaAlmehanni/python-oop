class Car(object):
	def __init__(self,name,year):
		self.name=name
		self.year=year

	def __str__(self):
		return str(self.name)+" "+str(self.year)

	def get_name(self):
	 	return self.name

	def get_year(self):
		return self.year

	def set_name(newName):
		self.name=newName

	def set_year(newYear):
		self.year=newYear
				 		
		