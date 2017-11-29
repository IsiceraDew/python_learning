"""
Random Number Generator
"""
import time
import datetime
import random


seed = int(datetime.datetime.now().microsecond)

def myrand():
	global seed
	seed *= 104333401
	seed += 714987293
	return seed % 256

def rchr():
	return chr(random.randint(0,255))

def rstring(length):
	l = list()
	for i in xrange(length):
		l.append(rchr())
	return "".join(l)
