"""
Fizzbuzz
"""



def NumCheck(x):
	if x % 3 == 0 and x % 5 ==0:
		print "Fizz Buzz"
	elif x % 3 == 0:
		print "Fizz"
	elif x % 5 == 0:
		print "Buzz"
	else: 
		print x

x = 1

while x <= 100:
	NumCheck(x)
	x = x + 1