"""
Genetic Algorithm
"""
import random
import rng

target_phrase = "The night is young and full of rest."
length = len(target_phrase)
pop_size = 5000

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
    fitness = []
    for c in creatures:
        fitness.append((fit_calc(c), c))
    fitness.sort()
    organized = []
    for f in fitness:
        organized.append(f[1])
    return organized    

def remove_worst(creatures):
    """Removes some of the worst creatures.
    Must always return a non-empty list.
    
    Input is a sorted list.
    """
    return creatures[:pop_size]

def create_offspring(creatures):
    """Create some offspring through mutation and / or crossover."""
    mutants = []
    for c in creatures:
        i = random.randint(0,length-1)
        mutant = c[:i] + rng.rchr() + c[i+1:]
        mutants.append(mutant)
    return mutants
        

result = run_genetic_algo(5000)

print "Winner:"
print result[0]