"""
Genetic Algorithm
"""

import rng
target_phrase = "The night is young and full of rest."
length = len(target_phrase)
pop_size = 50

def run_genetic_algo(num_steps):
    creatures = init_creatures()

    for i in xrange(num_steps):
        creatures = sort_by_fitness(creatures)
        print "Iteration {}:".format(i)
        print creatures[0]
        print "Fitness{}:", fit_calc(creatures[0])
        creatures = remove_worst(creatures)
        children = create_offspring(creatures)
        creatures += children
        
    return creatures

def init_creatures():
    """Returns a list of random strings of length length."""
    c = []
    for i in xrange(pop_size):
        c.append(rng.rstring(length))
    return c

def fit_calc(creature):
    fitness = 0
    for i in xrange(len(creature)):
        if creature[i] == target_phrase[i]:
            fitness -= 1
    return fitness


def sort_by_fitness(creatures):
    """Returns the input list of creatures sorted by fitness, i.e.,
    creatures[0] is the fittest."""
    return creatures  # TODO: placeholder

def remove_worst(creatures):
    """Removes some of the worst creatures.
    Must always return a non-empty list.

    Input is a sorted list.
    """
    return creatures  # TODO: placeholder (homework possibility)

def create_offspring(creatures):
    """Create some offspring through mutation and / or crossover."""
    return []  # TODO: placeholder

result = run_genetic_algo(8)

print "Winner:"
print result[0]