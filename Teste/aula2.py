a = float(input('Coloque o valor de a: '))
b = float(input('Coloque o valor de b: '))
c = float(input('Coloque o valor de c: '))

delta = b**2 - 4 * a * c

if delta > 0 :
    print('A equação produz duas raizes reais.')
elif delta == 0 :
    print('A equação produz uma raiz real.')
else :
    print('A equação não produz razes reais.')

print('**********FINALIZADO**********')
"""
DESAFIO:

Sabendo que o delta de uma equação do segundo grau (ax^2 + bx + c = 0) pode ser calculado através da formula delta = b^2 - 4*a*c. Sabendo que ainda que:

Se delta > 0: A equação produz duas raizes reais.
Se delta == 0: A equação produz uma raiz real.
Se delta < 0: A equação não produz razes reais.
Faça um programa em python que receba do usuário (input) os coeficientes da equação (a, b, c) e informe quantas raizes reais a equação possui.

Obs.: O Python possui o operador '**' que faz a potência de um numero por outro. Exemplo: a**2 é o mesmo que a ao quadrado.
"""