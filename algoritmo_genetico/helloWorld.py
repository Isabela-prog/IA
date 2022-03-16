import random
import datetime


geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = "Hello World!"

# Geração pai
def generate_parent(length):
    genes = []
    while len(genes) < length:
        # Gerar o menor "tamanho" entre os parâmetros
        sampleSize = min(length - len(genes), len(geneSet))
        # Adiciona os elementos a lista genes
        # sampleSize -> tamanho da amostra
        # geneSet -> de onde serão tirado os elementos, aleatoriamente
        genes.extend(random.sample(geneSet, sampleSize))
    return ''.join(genes)

# Avaliação de aptidão
def get_fitness(guess):
    # Verifica se as letras do cromossomo gerado estão na mesma possição da senha, soma 1
    # Soma 1, essa será a avaliação -> melhor avaliado é o 12
    return sum(1 for expected, actual in zip(target, guess) if expected == actual)

# Troca uma letra do cromossomo por uma letra aleatória, gerando mutações
def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)

    # Evita repetições
    if newGene == childGenes[index]:
        childGenes[index] = alternate 
    else:
        newGene
    # print('childGenes', childGenes)
    return ''.join(childGenes)
    
# "Print"
def display(guess):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(guess)
    print("{0}\t{1}\t{2}".format(guess, fitness, str(timeDiff)))

random.seed()
startTime = datetime.datetime.now()
# Geração pai
bestParent = generate_parent(len(target))
bestFitness = get_fitness(bestParent)
display(bestParent)

# loop que vai fazer todo código rodar, enquanto todas as letras do mais apto não forem iguais as de target
# Compara o filho anterior com o atual, mantém ou substitui
while True:
    child = mutate(bestParent)
    childFitness = get_fitness(child)

    if bestFitness >= childFitness:
        continue
    display(child)
    if childFitness >= len(bestParent):
        break
    bestFitness = childFitness
    bestParent = child