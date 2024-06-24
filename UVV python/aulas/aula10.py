"""

lista = []
nomes = {}
nomes["nome"] = input('Coloque o nome aqui ==> ')
lista.append(nomes)
print(lista)

"""

import random as rd # Contém funções para trabalhar aleatoriedade
#trabalhar com arrays

jogador_dict = {} #Criando um dicionário vazio para armazenar os jogares e suas tentativas
opcao = 'n' #Atribuindo valor "n"

while opcao != 'S': #Aqui estamos controlando o valor digitado pelo usuário. Tem que ser inteiro válido
    
    #Boas Vindas ao "Desafiante"
    print("Vamos fazer uma disputa? Tente descobrir o número que estou pensando.")
    print()
    print("""
    Primeiro você irá escolher quantas tentativas você irá ter para descobrir meu número. \n
    Depois você irá dizer quais são os limites mínimos e máximos para os números que eu posso escolher!! \n
    Boa sorte!!
    """)
    print ()
    
    chances = '' #"Zerando" a variável
    minimo = '' #"Zerando" a variável
    maximo = '' #"Zerando" a variável
    
    """
        Vamos criar um Dicionário para armazenar o nome do jogador e a quantidade de tentativas que ele precisou para vencer o
        computador.
        Não iremos controlar se o jogador já existe ou não dentro dos registros. Apenas iremos armazenar para posteriormente
        exibir o resultado.
    """
    jogador = input("Digite o seu nome meu caro desafiante: ")
    print()
    
    while chances == '': #Aqui estamos controlando o valor digitado pelo usuário. Tem que ser inteiro válido

        """
        O try e except são tratamento de excessões. 
        A instrução try funciona da seguinte maneira:

        Primeiramente, a cláusula try (o conjunto de instruções entre as palavras reservadas try e except ) é executada.

        Se nenhuma exceção ocorrer, a cláusula except é ignorada e a execução da instrução try é finalizada.

        Se ocorrer uma execução durante a execução da cláusula try, as instruções remanescentes na cláusula são ignoradas. 

        Se o tipo da exceção ocorrida tiver sido previsto em algum except, então essa cláusula será executada. 

        Depois disso, a execução continua após a instrução try.

        A instrução try pode ter uma ou mais cláusula de exceção, para especificar múltiplos tratadores para diferentes exceções.
        """  
        try:
            chances = input("Digite a quantidade de chances que você quer para tentar me vencer: ")
            chances = int(chances)            
        except:
            chances = ''
            print("Digite um número inteiro válido, por favor!! \n")
    
    while minimo == '': #Aqui estamos controlando o valor digitado pelo usuário. Tem que ser inteiro válido
        try:
            minimo = input("Digite o valor mínimo que eu posso escolher: ")
            minimo = int(minimo)            
        except:
            minimo = ''
            print("Digite um número inteiro válido, por favor!! \n")

    while maximo == '': #Aqui estamos controlando o valor digitado pelo usuário. Tem que ser inteiro válido
        try:
            maximo = input("Digite o valor máximo que eu posso escolher: ")
            maximo = int(maximo)
            print()
        except:
            maximo = ''
            print("Digite um número inteiro válido, por favor!! \n")
            print()

    #Usando placeholder para informar ao usuário o "range" de números que o computador pode escolher
    print("Eu irei escolher um número entre %d e %d, OK?" %(minimo, maximo))


    
    exibir = np.arange(minimo, maximo + 1)
    num_aleatorio = rd.randrange(minimo, maximo + 1) #O valor máximo é exclusivo, por isso adicionamos 1
        
    cont = 1 #Contador para o número de tentativas
    
    print(exibir)
    print
    try:  
        num_tentativa = input('tentativa %d: ' %cont)
        num_tentativa = int(num_tentativa)
        
    except:
        num_tentativa = ''
        print('Digite um número inteiro válido.')
    
                
    if num_tentativa!= '': #Após digitar um valor válido entramos nas condicionais para "descobrir o valor"
        while num_tentativa!= num_aleatorio and cont < chances:
                if num_tentativa == num_aleatorio:
                    break

                elif num_tentativa < num_aleatorio:
                    print('o numero é mais alto(+): ')
                    print()
                    #Aqui estamos criando um array com os números que serão retirados da nossa lista para exibir ao usuário
                    faixa_ret = np.arange(min(exibir),num_tentativa + 1)
                    if len(exibir) > len(faixa_ret):
                        #A função setdiff1d retira do array "exibir" os objetos do array "faixa_ret"
                        #A condicional if é devido a função setdiff1d. Ela retira do array maior os objeos do array menor
                        exibir_novo = np.setdiff1d(exibir,faixa_ret) 
                    else:
                        exibir_novo = np.setdiff1d(faixa_ret,exibir) 
                    print()

                elif num_tentativa > num_aleatorio and num_tentativa!='':
                    print('o numero é mais baixo(-): ')
                    print()
                    faixa_ret = np.arange(num_tentativa,max(exibir) + 1)
                    if len(exibir) > len(faixa_ret):
                        exibir_novo = np.setdiff1d(exibir,faixa_ret) 
                    else:
                        exibir_novo = np.setdiff1d(faixa_ret,exibir) 
                    print()
                    
                print('O número está entre estes: \n', exibir_novo, '\n')

                if num_tentativa!= '':
                    cont = cont + 1
                #Substituindo o array inicial "exibir" pelo array "exibir_novo" que é o resultado da diferença setdiff1d 
                exibir = exibir_novo
                
                num_tentativa = ''
                while num_tentativa == '':
                    try:
                        num_tentativa = input('tentativa %d: ' %cont)
                        print()
                        num_tentativa = int(num_tentativa)
                    except:
                        num_tentativa = ''
                        print('Digite um número inteiro válido: ')
                        print()
                        
        
        if cont == chances and num_tentativa!= num_aleatorio:
            #armazenando os dados do "perdedor" no dicionário
            jogador_dict[jogador] = [minimo, maximo, cont, num_aleatorio, "derrota"]
            print()
            print('%s suas chances acabaram e você perdeu!!!' %jogador)
            print('Você teve %d tentativas para descobrir um número entre %d e %d e infelizmente não conseguiu!!' %(jogador_dict[jogador][2],jogador_dict[jogador][0],jogador_dict[jogador][1]))
            print('O número era %d e a Máquina venceu!!' %num_aleatorio)
            print()
            print('Desafiantes que tentaram me vencer e não conseguiram!!')
            print("--------------------------------------------------------------------------------")
            print(f"{'Desafiante' : <20}|{'Tentativas' : ^10}|{'Faixa' : ^15}|{'O Número era' : >15}") 
            print("--------------------------------------------------------------------------------")
            #loop for para percorrer todos os dicionários e os dados armazenados
            for jogador, lista in jogador_dict.items():
                #condicional para exibir apenas os "vencedores"
                if jogador_dict[jogador][4] == "derrota":
                    #utilizando format para exibir o resultado. 
                    """
                    a marcação {NOME: <20 } siginifica que a variável NOME terá espaço reservado de 20 caracteres e o alinhamento
                    será à esquerda. para alinhar à direita, utilizar sinal de "maior" p.ex.: {NOME: >20} ou seja, 20 caracteres
                    reservados (no mínimo) com alinhamento à direita. Alinhamento central é o "^".
                    No nosso exemplo:
                    print(f'...') print para exibir na tela e o "f" é formatString - significa que o python respeitará formatação.
                    Dando sequencia no nosso exemplo: {jogador : <20} A chave "jogador", do dicionário que criamos, terá espaço de 20 caracteres,
                    independente se tiver menos de 20, o python reservará no mínimo 20 caracteres e irá alinhar os valores à esquerda.
                    {lista[2] : ^10} siginifica que estamos acessando o terceiro elemento da lista que criamos dentro do dicionário
                    (lembre-se que em python o índice começa em Zero) e estamos reservando no mínimo 10 caracteres e alinhando ao centro.
                    E assim por diante.
                    """
                    print(f'{jogador : <20}|{lista[2] : ^10}|{lista[0] : <6} a {lista[1] : >6}|{lista[3] : >15}')

        else:
            #armazenando os dados do "vencedor" no dicionário
            jogador_dict[jogador] = [minimo, maximo, cont, num_aleatorio, "vitoria"]
            print()
            print('Parabéns %s, você acertou!!! O número é: %d' %(jogador, num_aleatorio))
            print('Você acertou com %d tentativas um número entre %d e %d!!' %(jogador_dict[jogador][2],jogador_dict[jogador][0],jogador_dict[jogador][1]))
            print()
            print('Desafiantes que tentaram me vencer e tiveram sucesso!!')
            print("--------------------------------------------------------------------------------")            
            print(f"{'Desafiante' : <20}|{'Tentativas' : ^10}|{'Faixa' : ^15}|{'O Número era' : >15}") 
            print("--------------------------------------------------------------------------------")
            #loop for para percorrer todos os dicionários e os dados armazenados
            for jogador, lista in jogador_dict.items():
                #condicional para exibir apenas os "vencedores"
                if jogador_dict[jogador][4] == "vitoria":
                    print(f'{jogador : <20}|{lista[2] : ^10}|{lista[0] : <6} a {lista[1] : >6}|{lista[3] : >15}')
        
        #Permitindo ao usuário continuar no programa ou encerrar
    opcao = input('Para sair digite S. Para jogar novamente aperte qualquer tecla: ').upper()
    print()
    print("--------------------------------------------------------------------------------")