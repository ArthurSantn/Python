"""
Celsius = [-2.3, 0, 10, -15, -1, 3, 50, 22, -5.1, 33, 100, -100]

Fahrenheit = [ ((float(9)/5)*temp + 32) for temp in Celsius ]

print(Fahrenheit)

Celsius.sort()
Fahrenheit.sort()
print("Graus Celsius\t\tGraus Fahrenheit")
print("------------------------------------------------------")
for i, j in zip(Celsius, Fahrenheit):
    print("%f\t\t%f" %(i, j))
    
indice = int(input("A partir de qual elemento você deseja visualizar a lista? "))
print("Exibindo o resultado a partir do ",indice,"° elemento")
print("Graus Celsius\t\tGraus Fahrenheit")
print("------------------------------------------------------")
Celsius = Celsius[indice:]
Fahrenheit = Fahrenheit[indice:]
for i, j in zip(Celsius, Fahrenheit):
    print("%f\t\t%f" %(i, j))
    
"""

"""
tup = (1, 2, 3) 
lista = list(tup) #converte a tupla em lista
print(lista)
"""
"""
lista = [5, 2]*5 #multiplica com o valor do indice que é 1
print(len(lista))
"""

lista = [1,1,1,3,7,14,15,16,17]
lista[8:0:-2] #forma alternativa de utilizar o in range / start-stop-step
#Retorno [17, 15, 7, 1]