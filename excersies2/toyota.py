import Car from './car'

class Toyota(Car):
	def __str__(self):
		return "Our Car Name : "+str(self.name)+" and the model year : "+str(self.year)