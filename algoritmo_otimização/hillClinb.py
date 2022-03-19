'''
Algoritmo da Subida da Encosta, pode ser usado tanto para a minimização quanto para a maximização das soluções

Funcionalidade:
    - Gera solução randômica -> uma lista com opções de voos, de ida para Roma e de volta para todas as outras cidades, de forma aleatória
    - Procura pelos melhores vizinhos, comparando o custos
    - Escolhe o menor valor de custo
'''

import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose

# Nome das cidades e sigla dos aeroportos de cada viajante
peoples = [('Lisboa', 'LIS'),
           ('Madrid', 'MAD'),
           ('Paris', 'CDG'),
           ('Dublin', 'DUB'),
           ('Bruxelas', 'BRU'),
           ('Londres', 'LHR')]
#print(peoples[0])

# Aeroporto de Roma
destiny = 'FCO'

flights = {}

# Abrir dados do doc de voôs
for line in open('C:\\Users\\Isabela Santos\\Yappi Lab\\lab\\AI\\algoritmo_otimização\\calendarioVoos\\flights.txt'):
    #print(line)
    origin, destination, departure, arrival, price = line.split(',')
    # Não repete os mesmo voos, só adiciona os novos valores de saída, chegada e preço
    flights.setdefault((origin, destination), [])
    flights[(origin, destination)].append((departure, arrival, int(price)))

#print(flights)

def impress_flights(agenda):
    id_flight = -1
    total_price = 0

    # Acessar voos
    for i in range(len(agenda)//2):
        # Posição e coluna
        name = peoples[i][0]
        origin = peoples[i][1]
        id_flight += 1

        # Voo de ida
        going = flights[(origin, destination)][agenda[id_flight]]
        total_price += going[2]
        id_flight += 1

        # Voo de volta
        back = flights[(destination, origin)][agenda[id_flight]]
        total_price += back[2]

        print('%10s%10s %5s-%5s %3s %5s-%5s %3s' % (name, origin, going[0], going[1], going[2], back[0], back[1], back[2]))
        
    print('Preço Total: ', total_price)

def fitness_function(agenda):
    # Percorrer todas as posições
    id_flight = -1
    total_price = 0

    # Acessar voos
    for i in range(len(agenda)//2):
        # Posição e coluna
        origin = peoples[i][1]
        id_flight += 1

        # Voo de ida
        going = flights[(origin, destination)][agenda[id_flight]]
        total_price += going[2]
        id_flight += 1

        # Voo de volta
        back = flights[(destination, origin)][agenda[id_flight]]
        total_price += back[2]

    return total_price

# Voos (10 voos para cada um)
agenda = [1,0, 3,2, 7,1, 6,3, 2,4, 5,3]
#print(fitness(agenda))

# Para funções fitness próprias
fitness = mlrose.CustomFitness(fitness_function)
# Trabalhar com númers inteiros
# Length -> quantidade total de voos
# Maximize -> maximizar os valores. False -> menor valor da passagem
# Max_val -> quantidade de voos
problem = mlrose.DiscreteOpt(length=12, fitness_fn=fitness, maximize=False, max_val=10)
# A função já retorna sozinha a melhor 
best_solution, best_cost = mlrose.hill_climb(problem, random_state=1)
print(best_solution, best_cost)
print(flights[('BRU', 'FCO')])