def f(a, b):
	print("{1} {0}".format(a, b))


f(1, 0)
f(b=0, a=1)

args1 = [1, 0]
f(*args1)

args2 = {'a': 1, 'b': 0}
f(**args2)
