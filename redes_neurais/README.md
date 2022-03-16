- Cada neurônio recebe um número de inputs (entradas0)
- Cada entrada terá um peso -> ensinar o neurônio a resposta correta
- Passar os outputs do neurônio por uma fórmula, com pesos ajustados
- Comparar o resultado do neurônio com o output esperado, diferença entre eles -> erro (1)
- Reajustar pesos (2)

(1):
- Soma ponderada das entradas do neurônio
- Normalizar para que a entrada fique entre 0 e 1 (função Sigmoid)

(2):
- Derivada ponderada por erros (propagação de erro) -> erro*entrada do neurônio*gradiente da cruva de Sigmóide(*)

*:
- saída muito positiva ou negativa -> neurônio confiante de sua saída -> não é necessário reajustar o peso -> gradiente garante isso
- curva = output*(1 - output)

