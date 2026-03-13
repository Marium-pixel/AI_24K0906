import random

def fitness(x):
    return x**2 + 2*x

def decode(chromosome):
    return int(chromosome, 2)

def random_chromosome():
    return ''.join(random.choice('01') for _ in range(5))

def selection(population):
    population.sort(key=lambda c: fitness(decode(c)), reverse=True)
    return population[:2]

def crossover(parent1, parent2):
    point = random.randint(1, 4)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutation(chromosome):
    index = random.randint(0,4)
    mutated = list(chromosome)
    mutated[index] = '1' if mutated[index]=='0' else '0'
    return ''.join(mutated)

population = [random_chromosome() for _ in range(6)]

for generation in range(15):

    parents = selection(population)

    child1, child2 = crossover(parents[0], parents[1])

    if random.random() < 0.2:
        child1 = mutation(child1)
    if random.random() < 0.2:
        child2 = mutation(child2)

    population = parents + [child1, child2]

best = max(population, key=lambda c: fitness(decode(c)))
best_x = decode(best)
best_fit = fitness(best_x)

print("Best chromosome:", best)
print("Best value of x:", best_x)
print("Best fitness value:", best_fit)
