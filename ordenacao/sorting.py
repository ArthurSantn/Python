import random

lista = random.sample(range(1, 1000), 50)

def selection_sort(lista) :
    lista = random.sample(range(1, 1000), 50)
    n = len(lista)
    for j in range(n-1): #Loop de ordenação de elementos
        min_index =  j
        for i in range(n):
            if lista[i] < min_index:
                min_index = lista[i] #Aqui foi definido o menor número dentro do range do array "Lista"

        j = 0
        if lista [j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux

            print(lista)
            selection_sort(lista)
            print("\n Ordenação")