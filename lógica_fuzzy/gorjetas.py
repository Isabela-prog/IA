import sys
import numpy as np
# Biblioteca para trablhar a lógica de fuzzy em arrays
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Universo da variável antecedente e seu rótulo
quality = ctrl.Antecedent(np.arange(0, 11, 1), 'Qualidade')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'Serviço')
#print(quality.universe)

# Consequência / intervalo -> 0% a 20%
gratuity = ctrl.Consequent(np.arange(0, 21, 1), 'Gorjeta')
#print(gratuity.universe)

# Popular o universo(valores) nas categorias
quality.automf(number=3, names=['ruim', 'boa', 'saborosa'])
service.automf(number=3, names=['ruim', 'aceitável', 'ótimo'])
quality.view()
service.view()

gratuity.universe
# Função triangular (gráfico em 'triângulo')
# Começa, onde é o pico e até onde vai
gratuity['baixa'] = fuzz.trimf(gratuity.universe, [0, 0, 10])
gratuity['media'] = fuzz.trimf(gratuity.universe, [2, 10, 18])
gratuity['alta'] = fuzz.trimf(gratuity.universe, [10, 20, 20])
gratuity.view()

# Regras -> Fuzzy faz a intermediação entre categoria e classe
rule1 = ctrl.Rule(quality['ruim'] | service['ruim'], gratuity['baixa'])
rule2 = ctrl.Rule(service['aceitável'], gratuity['media'])
rule3 = ctrl.Rule(service['ótimo'] | quality['saborosa'], gratuity['alta'])

# Criar as notas
system_control = ctrl.ControlSystem([rule1, rule2, rule3])
system = ctrl.ControlSystemSimulation(system_control)

system.input['Qualidade'] = 10
system.input['Serviço'] = 6.5
system.compute()

print(system.output['Gorjeta'])
gratuity.view(sim = system)

