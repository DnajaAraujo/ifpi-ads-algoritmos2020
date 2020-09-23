def envia_idade_mae():
    print('>> Car Talk: Idade do filho \n')
    idade_mae = 0

    for i in range(60):
        idade_mae += 1
        valida_idade_mae(idade_mae)


def valida_idade_mae(idade_mae):
    conta_palindromo = 0
    idade_filho = 0
    nova_idade_mae = idade_mae
    
    for i in range(100):
        if eh_palindromo(idade_filho, nova_idade_mae):
            conta_palindromo += 1
            
            if conta_palindromo == 8:
                valida_idade_filho(idade_mae)

        idade_filho += 1
        nova_idade_mae += 1
    

def valida_idade_filho(idade_mae):
    idade_filho = 0
    conjunto_idades = ''
    
    for i in range(150):
        if eh_palindromo(idade_filho, idade_mae):
            conjunto_idades += str(idade_filho)
        
        idade_filho += 1
        idade_mae += 1
    
    mostra_idade(conjunto_idades)


def eh_palindromo(idade_filho, idade_mae):
    idade_filho = str(idade_filho)
    idade_filho = int(idade_filho[::-1])

    return idade_filho == idade_mae


def mostra_idade(conjunto_idades):
    tamanho = len(conjunto_idades)
    idade_atual = conjunto_idades[tamanho-6:tamanho-4]

    print(f'O filho tem {idade_atual} anos atualmente.')







