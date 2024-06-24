import random as rd #troca a palavra random por rd ==> Escopo/simplificar o código
import numpy as np #Ainda não sei por que o numpy não funciona aqui

lista = [1,2,3,4,5,6,7,8,9,10]
aleatorio = rd.choice(lista) #aqui ele pede pro rd (randomizador) escolher ".choice()" um número da lista.

print(aleatorio)



# Criar um array 1D
array1d = np.array([1, 2, 3, 4, 5])
print(array1d)

# Criar um array 2D (matriz)
array2d = np.array([[1, 2, 3], [4, 5, 6]])
print(array2d)

# Criar um array de zeros
zeros = np.zeros((2, 3))
print(zeros)

# Calcular a média de um array
media = np.mean(array1d)
print(media)

# Realizar operações aritméticas com arrays
soma = array1d + 10
print(soma)