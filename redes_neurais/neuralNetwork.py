from numpy import exp, array, random, dot
from pip import main

class NeuralNetwork():
    def __init__(self):
        # Gerar sempre o mesmo resultado
        random.seed(1)

        # Atribuir pesos aleatórios a uma matriz, variando entre -1 e 1
        self.synaptic_weights = 2 * random.random((3, 1)) - 1

    # Normaliza entre 0 e 1
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))
    
    # Derivada da curva sigmoide
    # Mostra o quanto confiante é o neurônio
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # Treinar o neurônio
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            output = self.think(training_set_inputs)

            # Verifica o erro do neurônio a partir da diferença entre a saída e a saída esperada
            error = training_set_outputs - output
            print('Erro para reajuste de pesos: ')
            print(error, '\n')

            # Ajuste dos pesos a partir do erro e da curva de sigmoide
            adjustment = dot(training_set_inputs.T, error*self.__sigmoid_derivative(output))

            self.synaptic_weights += adjustment
    
    # Passa as entradas para rede neural
    # Soma ponderada dos erros
    def think(self, inputs):
        return self.__sigmoid(dot(inputs, self.synaptic_weights))

if __name__ == "__main__":
    # Incializa um neurônio
    neural_network = NeuralNetwork()

    print("Pesos sinápticos aleatórios: ")
    print(neural_network.synaptic_weights, '\n')

    # Entrada do neurônio
    training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    # Saída
    # Transpor matriz
    training_set_outputs = array([[0, 1, 1, 0]]).T

    neural_network.train(training_set_inputs, training_set_outputs, 10000)

    print('Nova sinapse, pós treinamento: ')
    print(neural_network.synaptic_weights, '\n')

    print('Nova situação, [1, 0, 0]: ')
    print(neural_network.think([1, 0, 0]), '\n')