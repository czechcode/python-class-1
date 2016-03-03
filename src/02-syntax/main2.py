
def main():
	print("Hello World!")

	name = "Felix"
	age = 24
	print("My name is {}, and I'm {} years old".format(name, age))


def types():
	s = "5"
	i = int(s)
	f = float(s)

	print(type(s))
	print(type(i))
	print(type(f))

def lists():
	tuple = (1, 2, 3)
	print(tuple)

	list = [1, 2, 3]
	print(list)

	dict = {'audi': 15000, 'tesla': 20000}
	print(dict)

lists()
