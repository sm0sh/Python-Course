def factorial(n):
	
	if n == 0:
		return 1
	
	return n * factorial(n-1)

num = 7;
print("Factorial of", num, "is",
factorial(num))
