'Os vetores ordenados são de grande importância na resolução dos problemas de algoritmos de busca'

from sys import last_traceback
from turtle import position, up
import numpy as np

class OrderedVector:
    
    def __init__(self, capicity):
        self.capacity = capicity
        self.last_position = -1
        # Gerar uma matriz apenas com int
        self.values = np.empty(self.capacity, dtype=int)
    
    def impress(self):
        if self.last_position == -1:
            print('Vetro vazio')
        else:
            for i in range(self.last_position + 1):
                print(i, ' - ', self.values[i])
    
    def insert(self, value):
        # Vetor cheio
        if self.last_position == self.capacity - 1:
            print('Capacidade máxima atingida')
            return
    
        position = 0
        # Procurar o número maior do que o inserido para poder mover o vetor
        for i in range(self.last_position + 1):
            position = i
            # Posição encontrada
            if self.values[i] > value:
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
        self.values[position] = value
        self.last_position += 1
