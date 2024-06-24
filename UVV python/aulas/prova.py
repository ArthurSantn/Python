""""
n = 1

while n < 10:
  n += 1
  print (n)
  
"""

"""
while True:
    print('1 - Cadastrar usuário\n2 - Logar usuário\n0 - Sair')
    escolha = int(input('Selecione uma opção ==>'))
    if escolha == 1:
      pass
    elif escolha == 2:
       pass
    else:
       break
"""

"""
senha_correta = 's3nha'
senha = ""

while senha != senha_correta:
  senha = input('Coloque sua senha aqui ==> ')
  print('senha errada')

print('Hello word')
"""

"""
senha_minima = 0
senha_maxima = 10
senha = 11

while senha < senha_minima or senha > senha_maxima:
  senha = int(input('Coloque sua senha aqui ==> '))
  if senha < senha_minima or senha > senha_maxima:
      print('senha errada')

print('Passou')

"""

"""
while True:
    entrada = input("Digite 'sair' para sair do programa, caso queira conmtinuar digite qualquer coisa: ")
    if entrada == "sair":
      break
    else:
       print('Você digitou ==> ', entrada)
"""

"""
numeros = [-1, -2, -3, -4, -5, -6, 4, -10]

indice = 0 

while indice < len(numeros):
    if numeros[indice] > 0:
        print('Parece que o primeiro número positivo da lista é ==> ', numeros[indice])
        break
    indice += 1
"""

#*******************S-u-P-E-R C-A-L-C-U-L-A-D-O-R-A 3_0_0_0****************************
continuar = 'sim'

while continuar == 'sim':
    n1 = float(input('Digite o primeiro número da conta ==> '))
    operacao = input('Digite a operaça que será utilizada (+, -, *, /) ==> ')
    n2 = float(input('Digite o segundo número da operação ==> '))
    if operacao == '+':
      print('***R E S P O S T A***\n', n1, '+', n2, '\n', '==> ' , n1 + n2, ' <==')
    elif operacao == '-':
      print('***R E S P O S T A***\n', n1, '-', n2, '\n', '==> ' , n1 - n2, ' <==')
    elif operacao == '*':
      print('***R E S P O S T A***\n', n1, '*', n2, '\n', '==> ' , n1 * n2, ' <==')
    elif operacao == '/':
      print('***R E S P O S T A***\n', n1, '/', n2, '\n', '==> ' , n1 / n2, ' <==')
    else:
      print('Operação inválida, tente novamente...')
    continuar = input("Deseja realizar outra operação? sim/não: ")
    if continuar == 'sim':
      pass
    else:
      break

"""
nomes = ['Arthur', 'Alexandre', 'Silvânia', 'Marcos', 'Macaco']
nome = input('Digite o nome da pessoa que está presente na lista ==> ')

for nome in nomes:
    if nome != nomes:
        print('Esse nome ', nome,' não esta na lista')
        break
    else:
        print(nome, 'está na lista')
"""
"""
nomes = ['Arthur', 'Alexandre', 'Silvânia', 'Marcos', 'Macaco']
posicao = 0
nome = input("Coloque o 'nome' da pessoa presente na lista ==> ")

while nomes[posicao] != nome:
  if nomes[posicao] != nome:
    print('O nome de ', nome, 'não está presente na lista')
    break
  else:
    print('O nome ', nome, ' está presente na lista')
    break
"""

"""
alunos = ['arthur', 'marcos', 'gabriel', 'claudia', 'cleiton']
lista = [1, 4, 5, 8, 2, 6, 3, 10]

print(alunos)
print(alunos[1])

alunos.append("carlos")
print('.APPEND() ==> ' , alunos)

alunos.insert(1, "arroz")
print('.INSERT(1, "") ==> ' ,alunos)

alunos.remove("arthur")
print('.REMOVE() ==> ' , alunos)

popvar = alunos.pop(2)
print('.POP() ==> ', alunos)
print(popvar)

alunos.sort()
print(alunos)

copiadalista = alunos.copy()

print(copiadalista)

index = alunos.index("cleiton")
print(index)

alunos.extend(lista)
print(alunos)

alunos.clear()
print(alunos)
"""
#--> append = Insere na última posição da lista
#--> insert(indice, "informação") = insere a informação da posição selecionada 
#--> remove("informação presente na lista") = Tira uma informação presente na lista
#--> pop(indice) = Remove o elemento da posição escolhida ===> e pode retornar o elemento removido <===
#--> sort() = Organiza em ordem aufabética ou numérica a lista
#--> reverse() = inverte a ordem de informações atual da lista
#--> clear() = Limpa a lista
#--> copy() = copia a lista
#--> count() = conta a quantidade de elementos na lista
#--> index = Diz o indice de um elemento presente na lista
#--> extend() = Cola uma lista na outra