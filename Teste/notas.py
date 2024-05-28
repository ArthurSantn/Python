print('===>Digite as notas do aluno 1 <===')
def Nota_AOP_1():
    while True: 
        campo1 = input("Digite a nota do aluno AOP 1 ==> ")
        campo1 = campo1.replace(',','.')
        nota1 = float(campo1)

        if nota1 < 0 or nota1 > 1:
            print('A nota deve ser entre 0 e 1')
        else:
            return nota1

nota1 = Nota_AOP_1()
print('A nota da AOP 1 foi,', nota1)

def Nota_AOP_2():
    while True:
        campo2 = input("Digite a nota do aluno AOP 2 ==> ")
        campo2 = campo2.replace(',','.')
        nota2 = float(campo2)

        if nota2 < 0 or nota2 > 2:
            print('A nota deve ser entre 0 e 2')
        else:
            return nota2

nota2 = Nota_AOP_2()
print('A nota da AOP 2 foi,', nota2)

def Nota_AOP_3():
    while True:
        campo3 = input("Digite a nota do aluno AOP 3 ==> ")
        campo3 = campo3.replace(',','.')
        nota3 = float(campo3)

        if nota3 < 0 or nota3 > 1:
            print('A nota deve ser entre 0 e 1')
        else:
            return nota3

nota3 = Nota_AOP_3()
print('A nota da AOP 2 foi,', nota3)

print('As notas foram, ' , nota1, nota2, nota3)


"""
aluno1 = []
aluno2 = []
aluno3 = []
aluno4 = []
aluno5 = []

for loopdecinco in range(4):
    print('===>Digite as notas do aluno', loopdecinco + 2,'<===')

    nota1 = Nota_AOP_1()
    if nota1 is not None:
        aluno1.append(nota1)

    nota2 = Nota_AOP_2()
    if nota2 is not None:
        aop2.append(nota2)

    nota3 = Nota_AOP_3()
    if nota3 is not None:
        aop3.append(nota3)
"""













"""
DESCRIÇÃO DO PROBLEMA: SISTEMA DE AVALIAÇÃO - UVVON
Faça um algoritmo em Python que leia de cem (100) alunos de um curso EAD da UVV:
LER DO USUÁRIO: Nota [0, 1] na AOP1: Atividade Online Pontuada 1;
LER DO USUÁRIO: Nota [0, 2] na AOP2: Atividade Online Pontuada 2;
LER DO USUÁRIO: Nota [0, 1] na AOP3: Atividade Online Pontuada 3;
LER DO USUÁRIO: Nota [0, 6] da PROVA REGULAR;
LER DO USUÁRIO: Nota [0, 10] da PROVA DE RECUPERAÇÃO: Somente se o aluno não obteve Soma do Módulo (AOP1 + AOP2 + AOP3 + Prova Regular) >=7
E, calcule e mostre na tela: as informações a seguir:
Soma do Módulo (SM) = AOP1 + APO2 + AOP3 + PROVA REGULAR
Média do Módulo (MM) = (AOP1 + APO2 + AOP3 + PROVA REGULAR + PROVA DE RECUPERAÇÃO)/2
EXIBIR:
Status do Aluno: Aprovado, Prova de recuperação ou Reprovado;
A quantidade de alunos (em porcentagem) que foram: Aprovado ou Reprovado;
Lembrando que, é considerado com Status Aprovado, o aluno que:
Obteve Soma do Módulo (SM) >= 7.0 ou
Obteve Média Módulo (MM) >= 5.0
Observações:
Para testar seu programa reduzir a quantidade de alunos da turma para 5 alunos, apenas.
É IMPORTANTE realizar a validação das notas inseridas pelo usuário. Não existem notas negativas, e, igualmente, não podemos aceitar notas que excedam o valor máximo estabelecido. Ex: Se o usuário digitar nota da AOP1 = -4, o programa precisa alertar e solicitar que digite um número válido entre 0-1.
Dica crucial: É fundamental seguir rigorosamente as solicitações do cliente, uma vez que esses requisitos são essenciais para o correto funcionamento do sistema. Evite excessos e não crie funcionalidades ou situações que não tenham sido expressamente requisitadas pelo cliente.
USAR ESTE MODELO COLAB - OBRIGATÓRIO: Link Aqui!
COMO ENTREGAR A AOP2?
Salve uma cópia deste arquivo com o “<SEU_NOME>-AOP2”.
Após desenvolver a atividade, salvar gere e envie exclusivamente o link de compartilhamento do seu código. 
Certifique-se de configurá-lo como público, pois só assim poderei realizar a correção. 
Observações:
Caso o link esteja privado, não poderei efetuar a avaliação da sua AOP, e sua atividade será considerada nula.
Após o envio da atividade e o início do processo de avaliação, a mesma fica bloqueada para edições.
"""