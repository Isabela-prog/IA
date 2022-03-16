
'''
Estudo de caso, achar a melhor rota de Arad a Bucareste

Usar heuristica a somatória da distância em linha reta e a distância pela estrada -> custo:
    - olhar para adjascentes de Arad
    - Ver qual deles tem o menor custo
    - Olhar seus adjascentes, repitir o processo
obs.: quando Bucharest é um vértice de uma cidade, considerar a distância em linha reta como zero 
'''
import numpy as np

class Vertex:
    def __init__(self, label, objective_distance):
        # Nome das cidades
        self.label = label
        self.visited = False
        # Adicionar cidades adjascentes, com quais cidades existe uma ligação
        self.adjacents = []
        # Distancia em linha reta
        self.objective_distance = objective_distance 
    
    def add_adjacent(self, adjacent):
        self.adjacents.append(adjacent)
    
    def print_adjacent(self):
        for i in self.adjacents:
            print(i.vertex.label, i.cost)

class Adjacent:
    def __init__(self, vertex, cost):
        self.vertex= vertex
        self.cost = cost

        self.astar_distance = vertex.objective_distance + self.cost
    
class Grafo:
    arad = Vertex('Arad', 366)
    zerind = Vertex('Zerind', 374)
    oradea = Vertex('Oradea', 380)
    sibiu = Vertex('Sibiu', 253)
    timisoara = Vertex('Timisoara', 329)
    lugoj = Vertex('Lugoj', 244)
    mehadia = Vertex('Mehadia', 241)
    dobreta = Vertex('Dobreta', 242)
    craiova = Vertex('Craiova', 160)
    rimnicu = Vertex('Rimnicu', 193)
    fagaras = Vertex('Fagaras', 178)
    pitesti = Vertex('Pitesti', 98)
    bucharest = Vertex('Bucharest', 0)
    giurgiu = Vertex('Giurgiu', 77)

    # Adicionar os adjacentos, junto do "custo" (km)
    arad.add_adjacent(Adjacent(zerind, 75))
    arad.add_adjacent(Adjacent(sibiu, 140))
    arad.add_adjacent(Adjacent(timisoara, 118))

    zerind.add_adjacent(Adjacent(arad, 75))
    zerind.add_adjacent(Adjacent(oradea, 71))

    oradea.add_adjacent(Adjacent(zerind, 71))
    oradea.add_adjacent(Adjacent(sibiu, 151))

    sibiu.add_adjacent(Adjacent(oradea, 151))
    sibiu.add_adjacent(Adjacent(arad, 140))
    sibiu.add_adjacent(Adjacent(fagaras, 99))
    sibiu.add_adjacent(Adjacent(rimnicu, 80))

    timisoara.add_adjacent(Adjacent(arad, 118))
    timisoara.add_adjacent(Adjacent(lugoj, 111))

    mehadia.add_adjacent(Adjacent(lugoj, 70))
    mehadia.add_adjacent(Adjacent(dobreta, 75))

    dobreta.add_adjacent(Adjacent(mehadia, 75))
    dobreta.add_adjacent(Adjacent(craiova, 120))

    craiova.add_adjacent(Adjacent(craiova, 120))
    craiova.add_adjacent(Adjacent(craiova, 138))
    craiova.add_adjacent(Adjacent(craiova, 146))

    pitesti.add_adjacent(Adjacent(craiova, 146))
    pitesti.add_adjacent(Adjacent(sibiu, 80))
    pitesti.add_adjacent(Adjacent(pitesti, 97))

    fagaras.add_adjacent(Adjacent(sibiu, 99))
    fagaras.add_adjacent(Adjacent(bucharest, 211))

    pitesti.add_adjacent(Adjacent(rimnicu, 97))
    pitesti.add_adjacent(Adjacent(craiova, 138))
    pitesti.add_adjacent(Adjacent(bucharest, 101))

    bucharest.add_adjacent(Adjacent(fagaras, 211))
    bucharest.add_adjacent(Adjacent(pitesti, 101))
    bucharest.add_adjacent(Adjacent(giurgiu, 90))

class OrderedVector:
    
    def __init__(self, capicity):
        self.capacity = capicity
        self.last_position = -1
        # Gerar uma matriz apenas com int
        self.values = np.empty(self.capacity, dtype=object)
    
    def insert(self, adjacent):
        # Vetor cheio
        if self.last_position == self.capacity - 1:
            print('Capacidade máxima atingida')
            return
    
        position = 0
        # Procurar o número maior do que o inserido para poder mover o vetor
        for i in range(self.last_position + 1):
            position = i
            # Posição encontrada
            if self.values[i].astar_distance > adjacent.astar_distance:
                break
            # Posicionar no fim
            if i == self.last_position:
                position = i + 1

        x = self.last_position

        # implementação ocorre da última posição para a encontrada
        while x >= position:
            # Próxima posição recebe o valor atual
            self.values[x + 1] = self.values[x]
            x -= 1
        
        # Adicionar o valor encontrado
        self.values[position] = adjacent
        self.last_position += 1
    
    def impress(self):
        if self.last_position == -1:
            print('Vetor vazio')
        else:
            for i in range(self.last_position + 1):
                print(i, 'Cidade - ', self.values[i].vertex.label, '| Custo - ', self.values[i].cost, 
                        '| Distância em linha reta -', self.values[i].vertex.objective_distance, 
                        '| Somatória -', self.values[i].astar_distance)

class AStar:
    def __init__(self, objective):
        self.objective = objective
        self.found = False
    
    def search(self, actual):
        print('-----------')
        print('Ponto atual: {}'.format(actual.label))
        actual.visited = True

        # Fim da recursão
        if actual == self.objective:
            self.found = True
        else:
            ordered_vector = OrderedVector(len(actual.adjacents))
            for adjacent in actual.adjacents:
                if adjacent.vertex.visited == False:
                    # Não revisitar esse ponto
                    adjacent.vertex.visited = True
                    ordered_vector.insert(adjacent)
            ordered_vector.impress()

            if ordered_vector.values[0] != None:
                self.search(ordered_vector.values[0].vertex)
    


grafo = Grafo()
grafo.arad.adjacents
grafo.arad.adjacents[0].vertex.label, grafo.arad.adjacents[0].vertex.objective_distance
grafo.arad.adjacents[0].astar_distance, grafo.arad.adjacents[0].cost

vector = OrderedVector(4)
vector.insert(grafo.arad.adjacents[0])
vector.insert(grafo.arad.adjacents[1])
vector.insert(grafo.arad.adjacents[2])
print(vector.impress())

search_astar = AStar(grafo.bucharest)
print(search_astar.search(grafo.arad))

