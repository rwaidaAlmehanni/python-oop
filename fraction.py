class Fraction(object):
	def __init__(self,x,y):
		self.numerator=x
		self.denominator=y

	def __str__(self):
		return str(self.numerator)+"/"+str(self.denominator)

	def __add__(self,anotherF):
		totalNum=self.numerator*anotherF.denominator + self.denominator * anotherF.numerator
		totalDen=self.denominator*anotherF.denominator
		return Fraction(totalNum,totalDen)

	def __sub__(self,anotherF):
		totalNum=self.numerator*anotherF.denominator - self.denominator*anotherF.numerator
		totalDen=self.denominator*anotherF.denominator
		return Fraction(totalNum,totalDen)

f1=Fraction(2,3)
f2=Fraction(3,4)
f3=f1+f2
f4=f1-f2
print(f3)
print(f4)		
		


		
