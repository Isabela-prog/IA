Conceito básico algoritmo genético 

# Pseudo código
# cada repetição -> uma geração do algoritmo
T = 0

iniciarPopulação()
loop:
    avaliarPopulação()
    selecionarPais()
    recombinaçãoEMutação() -> operadores genéticos
    avaliarNovaPopulação()
    selecionarSobreviventes()

    T = T + 1

- A avaliacaçã da populão ocorre por meio de uma fórmula que dê pontuações a cada indivíduo, sendo assim, os melhores poderão ser selecionados
- A recombinação e/ou a mutação geram maior variabildade genética na população, o que é importante para aumentar o campo de soluções
- A seleção dos melhores sobreviventes garante que a evolução seja satisfatória
- Caso nenhum cromossomo satisfaça a melhor aptidão, ou o tempo máximo tenha sido atingido, novos pais deverão ser selecionados
