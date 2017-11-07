"""
Write a function that determines the maximal value in a non-empty list of integers.

E.g., find_max([1,2,3,4,5,6]) == 6
find_max([4, 1, 10, 2]) == 10
"""

def find_max(x):
	i = 0
	max_so_far = x[0]
	while i < len(x):
		if x[i] > max_so_far :
			max_so_far = x[i]
		i = i + 1
	return max_so_far

print "This should be 6:", find_max([1,2,6])
print "This should be 10:", find_max([4, 1, 10, 2])
print "This should be 200:", find_max([200, 4, 1, 10, 2])

