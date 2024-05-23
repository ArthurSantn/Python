def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 1:
                return nota
            else:
                print("A nota deve estar entre 0 e 1.")
        except ValueError:
            print("Digite um número válido entre 0 e 1.")

# Ler as notas
aop1 = ler_nota("Digite a nota da AOP1 (entre 0 e 1): ")
aop2 = ler_nota("Digite a nota da AOP2 (entre 0 e 2): ")
aop3 = ler_nota("Digite a nota da AOP3 (entre 0 e 1): ")
prova_regular = ler_nota("Digite a nota da Prova Regular (entre 0 e 6): ")

# Verificar se o aluno precisa fazer a Prova de Recuperação
if aop1 + aop2 + aop3 + prova_regular < 7:
    prova_recuperacao = ler_nota("Digite a nota da Prova de Recuperação (entre 0 e 10): ")
else:
    prova_recuperacao = 0

# Calcular SM e MM
sm = aop1 + aop2 + aop3 + prova_regular
mm = (aop1 + aop2 + aop3 + prova_regular + prova_recuperacao) / 2

# Determinar o status do aluno
if sm >= 7.0 or mm >= 5.0:
    status = "Aprovado"
elif prova_recuperacao > 0:
    status = "Prova de Recuperação"
else:
    status = "Reprovado"

# Exibir resultados
print(f"Soma do Módulo (SM): {sm:.2f}")
print(f"Média do Módulo (MM): {mm:.2f}")
print(f"Status do Aluno: {status}")

# Calcular porcentagem de alunos aprovados e reprovados (considerando 5 alunos)
total_alunos = 5
aprovados = 1 if status == "Aprovado" else 0
reprovados = 1 if status == "Reprovado" else 0
porcentagem_aprovados = (aprovados / total_alunos) * 100
porcentagem_reprovados = (reprovados / total_alunos) * 100

print(f"Porcentagem de alunos aprovados: {porcentagem_aprovados:.2f}%")
print(f"Porcentagem de alunos reprovados: {porcentagem_reprovados:.2f}%")