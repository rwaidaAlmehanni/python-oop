from human import Human 

class Employee(Human):
	def __init__(self,name,age,country,salary):
		super(Employee,self).__init__(self,name,age,country)
		self.salary=salary

	def __str__(self):
		return Human.__str__(self)+" "+str(self.salary)

	def get_salary(self):
		return self.salary

	def set_salary(newSalary):
		self.salary=newSalary

# x=Employee("Ali",28,"Jordan",5000)
# print(x)		

