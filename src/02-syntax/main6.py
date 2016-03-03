
class Car:
	def __init__(self):
		self.wheels = 4

	def __str__(self):
		return str(self.wheels)

	def render(self):
		print(self.wheels)

c = Car()
c.render()
print(c)