class MathDojo(object):

	def __init__(self):
		self.total = 0

	def add(self, *restOfArg):
		for i in restOfArg:
			if type(i) == int:
				self.total += i
			else:
				for j in i:
					self.total += j
		return self

	def subtract(self, *restOfArg):
		for i in restOfArg:
			if type(i) == int:
				self.total -= i
			else:
				for j in i:
					self.total -=j
		return self

	def result(self):
		print self.total
		return self

md = MathDojo()
md.add(1, [2,3], (4,5.6)).subtract(1, [2,3], (4,5)).result()
