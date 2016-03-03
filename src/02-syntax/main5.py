
def faktorial1(n):
	f = 1
	while(n > 1):
		f *= n
		n -= 1
	return f 

def faktorial2(n):
	f = 1
	for nx in range(1, n+1):
		f *= nx

	return f

def faktorial3(n):
	if (n<=1):
		return 1
	return n*faktorial3(n-1)

print("Faktorial: ", faktorial1(5))
print("Faktorial: ", faktorial2(5))
print("Faktorial: ", faktorial3(5))
