"""
O dicionário irá ter a estrutura Key como nome do entrevistado e itens IDADE, SEXO, CADIDATO

"""
entrevista = {}
#Criando a Lista de cadidatos:
candidatos = ["BREJA GELADA", "CANA BRAVA", "ZÉ DA PINGA"]

opcao = 'n' #Atribuindo valor "n" para continuar entrevista

#Boas Vindas ao Entrevista
print ("Olá! Tudo bem? Estamos fazendo um breve pesquisa para saber a intenção de voto nestas eleições.")
print ()
while opcao != 'S': #Aqui estamos controlando o valor digitado pelo usuário. Tem que ser inteiro válido
    
    
    idade = ''
    sexo = ''
    escolha = ''
    
    nome = input("Qual seu o nome? ")
    print()
    
    while idade == '':
        try:
            idade = input("Qual sua idade? ")
            idade = int(idade)            
        except:
            idade = ''
            print("Digite uma idade válida, por favor!! \n")
    
    while sexo == '':
        sexo = input("""
Você se considera de qual sexo?
            
 M - Masculino
 F - Feminino
 O - Outro não especificado anteriormente ou prefere não opniar
 
 Escolha: """)
        if sexo in ["M","m","F","f","O","o"]:
            sexo = sexo.upper()
            if sexo == "M":
                sexo = "Masculino"
            elif sexo == "F":
                sexo = "Feminino"
            else:
                sexo = "Não Binário"
        else: 
            sexo = ''

    
    while escolha == '':
        escolha = input("""
Dos candidatos abaixos, em quem você irá votar?
        
 1 - "BREJA GELADA"
 2 - "CANA BRAVA" 
 3 - "ZÉ DA PINGA"
            
Escolha: """)
        print()
        try:
            escolha = int(escolha)
        except:
            escolha = ''
            print()
            print("Digite um voto válido, por favor!! \n")

            
        if escolha != '' and escolha not in range (1,4):
            escolha = ''
            print()
            print("Escolha uma das opções de voto, por favor! \n")
            
        
    escolha = escolha - 1 #ajustando posição de índice
    entrevista[nome] = [idade, sexo, candidatos[escolha]] # criando o dicionário com os dados da entrevista
    
    #exibindo o resultado da votação individual
    print('%s de %d anos, do sexo %s, votou em %s' %(nome, entrevista[nome][0], entrevista[nome][1], entrevista[nome][2]))
    
    #exibindo o resultado da votação geral
    print()
    print("Situação da Votação")
    print("--------------------------------------------------------------------------------")
    print(f"{'Eleitor' : <40}|{'Idade' : ^7}|{'Sexo' : ^20}|{'Votou no Candidato' : >20}") 
    print()
    for nome, lista in entrevista.items():
        print(f'{nome : <40}|{lista[0] : ^7}|{lista[1] : ^20}|{lista[2] : >20}')
    print()
    opcao = input('Para encerrar a entrevista Digite "S", ou aperte qualquer tecla para continuar: ').upper()
