import os

class Car:
	
	staticVariable = 5
	#
	def __init__(self, enginePower, brand, maxSpeed):
		self.enginePower = enginePower
		self.brand = brand
		self.maxSpeed = maxSpeed
	#	
	def printcar(self):
		print(self.enginePower,self.brand,self.maxSpeed)
	#
	def getStaticVariable(self):
		return self.staticVariable
	
	#def __del__(self):
        #print("Destructor called, car deleted.")
	
		
c1 = Car('367/5600', 'Lexus', 210)
c2 = Car('270/5600', 'Impala', 220)
c3 = Car('235/5600', 'BMV', 260)

c1.printcar()
c2.printcar()
c3.printcar()

print(c1.getStaticVariable())

os.system("PAUSE")