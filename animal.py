# Practicing class inheritance 

class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def displayHealth(self):
		print "Name: {}; Health: {}".format(self.name, self.health)
		print "%" * 50
		return self

animal1 = Animal('Betty')
animal1.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
		print "I love pets!"
		self.health += 5
		return self

dog1 = Dog('Fido')
dog1.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health = 200
		print 'This is a dragon!'
	def fly(self):
		print "I'm as free as a bird!....ouch!"
		self.health -= 10
		return self

dragon1 = Dragon('Charizard')
dragon1.walk().walk().walk().run().run().fly().fly().displayHealth()
