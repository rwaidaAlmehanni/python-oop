class Human(object):
	def __init__(self,name,age,country):
		self.name=name
		self.age=age
		self.country=country

	def __str__(self):
		return str(self.name)+" "+str(self.age)+" "+str(self.country)

	def get_name(self):
	 	return self.name

	def get_age(self):
		return self.age

	def get_country(self):
	 	return self.country	

	def set_name(newName):
		self.name=newName

	def set_age(newAge):
		self.age=newYear

	def set_country(newCountry):
		self.country=newCountry	
				 		
		