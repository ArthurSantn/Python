"""
lista = ['0', '1', '2', '3', '4', '5']
lista.insert(2,'bungas')
lista.pop()
lista.append('Bangas')
print(lista)
"""

"""
print('Senha criptografada:', end=' ')
for contador in range(1000, 10000):
    if contador % 2 != 0 and contador % 29 == 0:
        print(f'{contador}')
        break
"""

"""
soma = 0
a, b = 0, 1
while True:
    soma = soma + a
    a, b = b, a + b
    if soma >= 10:
        break
print(f'A soma é {soma}')
"""
"""
semana = ['SEGUNDA-FEIRA', 'SEGUNDA-FEIRA', 'QUARTA-FEIRA', 'SÁBADO', 'SEXTA-FEIRA', 'DOMINGO']
semana.insert(1, 'TERÇA-FEIRA')
semana.pop(2)
semana.remove('SÁBADO')
semana.insert(3, 'QUINTA-FEIRA')
semana.insert(5, 'SÁBADO')

print(semana)
"""

lista = [['Arthur', 19, 'maio' , 2005], ['Aexandre', 28, 'agosto' , 1996], ['Silvânia', 50, 'abril' , 1940]]

listaMeses = [contato[2] for _, contato in enumerate (lista)]

print(contato)