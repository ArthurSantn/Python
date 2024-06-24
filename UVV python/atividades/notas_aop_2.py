def ler_nota(prompt, minimo, maximo):
    while True:
        try:
            nota = float(input(prompt))
            if minimo <= nota <= maximo:
                return nota
            else:
                print(f"Nota inválida! Digite um valor entre {minimo} e {maximo}.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")

def calcular_status(aop1, aop2, aop3, prova_regular, prova_recuperacao=None):
    sm = aop1 + aop2 + aop3 + prova_regular
    mm = (sm + (prova_recuperacao if prova_recuperacao is not None else 0)) / 2

    if sm >= 7.0:
        return 'Aprovado', sm, mm
    elif mm >= 5.0:
        return 'Aprovado', sm, mm
    elif prova_recuperacao is not None:
        if mm >= 5.0:
            return 'Aprovado', sm, mm
        else:
            return 'Reprovado', sm, mm
    else:
        return 'Prova de recuperação', sm, mm

def main():
    num_alunos = 5
    aprovados = 0
    reprovados = 0
    recuperacao = 0

    for i in range(1, num_alunos + 1):
        print(f"\nDigite as notas do aluno {i}:")

        aop1 = ler_nota("Nota AOP1 [0, 1]: ", 0, 1)
        aop2 = ler_nota("Nota AOP2 [0, 2]: ", 0, 2)
        aop3 = ler_nota("Nota AOP3 [0, 1]: ", 0, 1)
        prova_regular = ler_nota("Nota Prova Regular [0, 6]: ", 0, 6)

        status, sm, mm = calcular_status(aop1, aop2, aop3, prova_regular)

        if status == 'Prova de recuperação':
            prova_recuperacao = ler_nota("Nota Prova de Recuperação [0, 10]: ", 0, 10)
            status, sm, mm = calcular_status(aop1, aop2, aop3, prova_regular, prova_recuperacao)

        print(f"Status do Aluno {i}: {status}")
        print(f"Soma do Módulo (SM): {sm:.2f}")
        print(f"Média do Módulo (MM): {mm:.2f}")

        if status == 'Aprovado':
            aprovados += 1
        elif status == 'Reprovado':
            reprovados += 1
        else:
            recuperacao += 1

    total_alunos = num_alunos
    print("\nResultados Finais:")
    print(f"Percentual de Aprovados: {(aprovados / total_alunos) * 100:.2f}%")
    print(f"Percentual de Reprovados: {(reprovados / total_alunos) * 100:.2f}%")
    print(f"Percentual de Alunos em Recuperação: {(recuperacao / total_alunos) * 100:.2f}%")

if __name__ == "__main__":
    main()