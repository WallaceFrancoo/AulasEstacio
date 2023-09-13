import numpy as np
numericos = np.array ([1,2,3,4,5])
print(numericos.dtype) # Retorno será int32 pois todas as string são numericos!

# Caso queira conventer para string utilizar o dtype='S'

numericosString = np.array ([1,2,3,4,5], dtype='S')
print(numericosString.dtype)