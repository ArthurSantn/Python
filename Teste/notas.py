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
    print('ok')

nota2 = Nota_AOP_2()
print('A nota da AOP 1 foi,' nota1)

def Nota_AOP_3():
    campo3 = input("Digite a nota do aluno AOP 3 ==> ")
    campo3 = campo3.replace(',','.')
    return float(campo3)

Nota3 = Nota_AOP_3()

if nota2 < 0 or nota2 > 1:
    print('A nota deve ser entre 0 e 1')
else:
    print('ok')
