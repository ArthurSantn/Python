#inserção de informações na lista

"""
import os
lista = []

while True:
    print("1 - Cadastrar\n2 - Listar\n0 - sair")
    select = int(input("Selecione a opção desejada ==> "))
    if select == 0:
        break
    elif select == 1:
        lista.append(input('Informe o que deseja colocar na lista ==> '))
        os.system('cls' if os.name == 'nt' else 'clear')
    elif select == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(lista)
        input('.:Aperte <enter> para continuar:.')
        os.system('cls' if os.name == 'nt' else 'clear')
"""

import os
lista = []

while True:
    print("1 - Cadastrar\n2 - Listar\n0 - sair")
    select = int(input("Selecione a opção desejada ==> "))
    if select == 0:
        break
    elif select == 1:
        novo_aluno = {}
        novo_aluno["nome"] = input('Digite o nome do aluno ==> ')
        novo_aluno["idade"] = int(input('Digite a idade dele/a ==> '))
        novo_aluno["curso"] = input('Digite o curso que o aluno está ==> ')
        lista.append(novo_aluno)
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system('cls' if os.name == 'nt' else 'clear')
    elif select == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        for aluno in lista:
            print(aluno["nome"])
        input('.:Aperte <enter> para continuar:.')
        os.system('cls' if os.name == 'nt' else 'clear')


"""

x = 190
y = 12

print(f"{x} + {y} = {x + y}")

"""

"""

temperatura = int(input('Digite a temperatura na sala: '))

if temperatura <= 10:

  print(f"Congelante: {temperatura}")

if temperatura <= 20:

  print(f"Frio: {temperatura}")

if temperatura < 30:

  print(f"Quente: {temperatura}")

if temperatura >= 60:

  print(f"Queimando: {temperatura}")

"""

"""
a,b = 2,3

if a<b:

  a,b = b,a*a

else:

  b,a = a,b

if b>a:

  a = a+1

elif b<a:

  a,b = a+1,b+1

if a==b:

  print(a,b)

elif b>a:

  print(b)

elif b<a:

  print(a)

else:

  print("nada")
  """