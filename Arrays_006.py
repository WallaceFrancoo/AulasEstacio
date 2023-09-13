# Neste arquivo iremos verificar como utilizar duas Arrays com matrizes
import numpy as np

ntPortugues = np.array([['Wallace', '7'], ['Carlos', '8'], ['William', '9'], ['Rodrigo', '7']])
ntMatematica = np.array([['Wallace', '10'], ['Carlos', '7'], ['William', '6'], ['Rodrigo', '8']])

for x in ntMatematica:
    nome_mat = x[0]
    nota_mat = float(x[1])

    # Encontrar a nota correspondente na disciplina de Português
    for y in ntPortugues:
        if y[0] == nome_mat:
            nota_por = float(y[1])
            break

    # Calcular a média das notas
    media_notas = (nota_mat + nota_por) / 2
    print(f'A média das notas de {nome_mat} é: {media_notas}')