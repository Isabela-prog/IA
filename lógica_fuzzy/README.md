Diferente da lógica aristotélica, a lógica de Fuzzy não possui uma resposta binária (sim ou não), ela expande seus resultados para valores entre Verdadeiro e Falso.
Há um grau de pertinência.

Exemplo:
Custo BAIXO e benefício ALTO -> custo-benefíco ALTO
Custo ALTO e benefício ALTO -> custo-benefíco MÉDIO
Custo BAIXO e benefício BAIXO -> custo-benefíco MÉDIO
Custo ALTO e benefício BAIXO -> custo-benefíco BAIXO

Um custo benefício médio pode ser meio baixo ou meio alto, depende da pertinência estabelecida.

- Estudo de caso: Gorgetas

ENTRADAS:
    - Serviço -> nota entre 0 e 10 para o serviço (classificar em ruim, aceitável e ótimo)
    - Qualidade da comida -> nota entre 0 e 10 para a comida (classifciar em ruim, boa e saborosa)

SAÍDAS:
    - gorjeta -> entre 0% e 20%, quanto seria a gorjeta (classificar em baixa, media e alta)

REGRAS:
    - qualidade da comida RUIM ou serviço RUIM -> gorjeta BAIXA
    - qualidade serviço MEDIO -> gorjeta MEDIA
    - qualidade da comida BOA ou serviço BOM -> gorjeta ALTA
