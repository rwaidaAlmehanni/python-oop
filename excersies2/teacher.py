from employee import Employee 

class Teacher(Employee):
	def __init__(self,name,age,country,salary,specialty):
		super(Teacher, self).__init__(name,age,country,salary)
		self.specialty=specialty

	def get_specialty(self):
		return self.specialty

	def set_specialty(newSpecialty):
		self.specialty=newSpecialty

	def __str__(self):
		return str(self.name)+" , "+str(self.age)+" , "+str(self.country)+" , "+str(self.salary)+" , "+str(self.specialty)			

x=Teacher("Ali",28,"Jordan",5000,"Math")
print(x)		