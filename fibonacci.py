"""
Write a function that computes the nth fibonacci number.

e.g.,
fib(0) = 1
fib(1) = 1
fib(2) = 2
fib(3) = 3
fib(4) = 5
"""

cache = {}

def Fib(x):
	if x in cache:
		return cache[x]

	if x == 0:
		return 1
	elif x == 1:
		return 1
	elif x > 1:
		y = Fib(x - 1) + Fib(x - 2)
		cache[x] = y
		return y

for x in range(100):
	print Fib(x)