"""
Write and test a function that accepts two words and prints them to the screen
with first letter reversed.

E.g.,
swap("war", "peace") 
will print:
"par", "weace"
"""
w1 = "Language"
w2 = "Words"

def Swap(x, y):
	print x[0] + y[1:]
	print y[0] + x[1:]

Swap(w1, w2)