"""
Random Number Generator
"""
import time
import datetime



seed = int(datetime.datetime.now().microsecond)

def rand():
	global seed
	seed *= 104333401
	seed += 714987293
	return seed % 256
def rstring(length):
	l = list()
	for i in xrange(length):
		c = chr(rand())
		l.append(c)
	return "".join(l)
