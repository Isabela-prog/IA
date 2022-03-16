# o objetivo do algoritmo genético é gerar o indivíduo com todos os genes '1'

import random
import sys
from types import GenericAlias
from jinja2 import pass_environment

# Gerar os inivíduos
def generate_individual(gene_size):
    individual = ''
    # Escolhe aleatoriamente os genes do indivíduo
    for i in range(gene_size):
        individual += str(random.randint(0,1))
    return individual

# Gerar a população de indivíduos
def generate_population (population_size, gene_size):
    population = []
    for i in range(population_size):
        population.append(generate_individual(gene_size))
    return population

# Avaliação de aptidão
# Soma a quantidade de genes '1' no cromossomo de cada indivíduo
def fitness(individual):
    return sum(int(gene) for gene in individual)

# Selecionar pais por meio de torneio
# K é o tamnho do torneio
def parent_selection(population, population_size, k=3):
    parent = []

    for tournament in range(population_size):
        competitors = []
        for i in range(k):
            # Sortear um indície aleatório para competidor
            index = random.randint(0, population_size-1)
            competitors.append(population[index])

        # Pressupor que o melhor avaliado é o primeiro indivíduo, para poder fazer as comparações
        best_parent = fitness(competitors[0])
        winner = competitors[0]
        for i in range(1, k):
            evaluation = fitness(competitors[i])
            if evaluation > best_parent:
                best_parent = evaluation
                winner = competitors[i]
        parent.append(winner)

    return parent

# Gerar F2, população de filhos
def beget_children(parent, population_size, tax_crossover=1):
    new_population = []

    #pegar sempre dois pais
    for i in range(population_size//2):
        parent1 = random.choice(parent)
        parent2 = random.choice(parent)

        if random.random() < tax_crossover:
            # Cada indivíduo tem gene-1 pontos de corte
            cut = random.randint(1, (len(parent1)-1))
            # Pegar o ocmeço do gene de um pai com o final do gene do outro pai
            children1 = parent1[0:cut] + parent2[cut:]
            children2 = parent2[0:cut] + parent1[cut:]
            new_population.append(children1)
            new_population.append(children2)
        # Caso o número gerado seja maior que a taxa de crossover, adicionar os pais a nova população
        else:
            new_population.append(parent1)
            new_population.append(parent2)

    return new_population

def mutate(population, population_size, gene_size, tax_mutate=0.005):
    new_population = []

    for i in range(population_size):
        individual = ''
        for j in range(gene_size):
            # Número gerado aleatoriamente precisa ser menor do que a taxa de mutação
            if random.random() < tax_mutate:
                # Inverter o gene, se for '0' será '1' e se for '1' será '0'
                if population[i][j] == '0':
                    individual += '1'
                else:
                    individual += '0'
            # Caso o número gerado seja maior que a taxa de mutação, continua o mesmo gene
            else:
                individual += population[i][j]
        new_population.append(individual)

    return new_population

def best_individual(population, population_size):
    best_evaluation = fitness(population[0])
    best_index = 0

    for i in range(1, population_size):
        evaluation = fitness(population[i])
        if evaluation > best_evaluation:
            best_evaluation = evaluation
            best_index = i
    return population[best_index]

# Rodar: python3 oneMax.py <tamanho da população> <quantidade de genes> <taxa de crossover> <taxa de mutação> <gerações>
# Gerar parâmetros
population_size, gene_size = int(sys.argv[1]), int(sys.argv[2])
tax_crossover, tax_mutate = float(sys.argv[3]), float(sys.argv[4])
generations = int(sys.argv[5])

population = generate_population(population_size, gene_size)
for generation in range(generations):
    parent = parent_selection(population, population_size)
    new_population = beget_children(parent, population_size, tax_crossover)
    population = mutate(new_population, population_size, gene_size, tax_mutate)

best_individual = best_individual(population, population_size)

# Prints
print('População: ', generate_population(population_size, gene_size), '\n')
# Avaliações do indivíduo
for individual in population:
    print('Indivíduo: %s, Avaliação %d' % (individual, fitness(individual)))
print('\n')
# Pais, F1
print('F1: ', parent, '\n')
# Nova população, F2
print('F2 após mutação', population, '\n')
# Melhor indivíduo
print('Melhor indivíduo', best_individual, '\n')
print('Melhor avaliação', fitness(best_individual), '\n')