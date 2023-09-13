#Nesse arquivo iremos utilizar o Copy e o View

import numpy as np

notas = np.array(['6','7','9','10','5','7'])
print(notas)

#Para criar uma copia da Array Notas sem alterar o notas utilizar o copy

nt1 = notas.copy() #nt1 é como se fosse notas 1

nt1[1] = 9 # aqui estou alterando a 2 nota que era um '7' para um '9'

print(nt1)
# esse foi o resultado:
# ['6' '7' '9' '10' '5' '7']
# ['6' '9' '9' '10' '5' '7']

# Caso queira alterar até a array principal utilizar o view

ntAll = notas.view()
ntAll[0] = 10

print(notas)
print(ntAll)
# Esse foi o resultado:
#['10' '7' '9' '10' '5' '7']
#['10' '7' '9' '10' '5' '7']

