import random
from sorting import selection_sort

aleatorio = random.sample(range(1,1000), 50)

ordered = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15]

if __name__ == "__main__":
    lista = aleatorio
    print(lista)
    selection_sort(lista)
    print("\n")