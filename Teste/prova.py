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

continuar = 'sim'

while continuar == 'sim':
  try:
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
     

  continuar = input("Deseja realizar outra operação? sim/não: ").lower()
  except ValueError:
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