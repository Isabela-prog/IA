import random
from re import S

population_size = 10
gene_size = 12

def generate_individual(gene_size):
    gene = ''
    for i in range(gene_size):
        gene += str(random.randrange(0,2))
    return gene

def generate_population (population_size):
    population = []
    for i in range(population_size):
        population.append(generate_individual(gene_size))
    return population

population = generate_population(population_size)
for i in range(generate_population):
    print(population[i])

