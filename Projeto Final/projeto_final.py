import os
import json


def main():
    # inicializar (recuperando do banco de dadaos)
    celulares = inicializar('celulares.bd')

    menu = tela_principal()
    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            celular = novo_celular()
            celulares.append(celular)
            print('\nCelular cadastrado com sucesso!')

        elif opcao == 2:
            mostra_celulares(celulares)
        
        elif opcao == 3:
            buscador = input('Digite o nome do modelo ou da marca do celular: ')
            resultado = encontra_celular(buscador, celulares)
            mostra_resultados_pesquisa(resultado)
            main2('celulares.bd', celulares, buscador)

        input('<enter> to continue...\n')
        opcao = int(input(menu))

    # finalizar (salvar banco)
    finalizar('celulares.bd', celulares)


def tela_principal():
    menu = '\n***** App Jobs Cell*****\n'
    menu += '1 - Cadastrar novo celular\n'
    menu += '2 - Listar todos os celulares\n'
    menu += '3 - Pesquisar celulares por nome\n'
    menu += '0 - Sair\n'
    menu += '\nOpçao >>> '
    
    return menu
        

def inicializar(nome_arquivo):
    celulares_carregados = []

    if os.path.exists(nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        dados = arquivo.readline()
        arquivo.close()
        celulares_carregados = json.loads(dados)
        
    return celulares_carregados


def finalizar(nome_arquivo, celulares):
    dados = json.dumps(celulares)

    arquivo = open(nome_arquivo, 'w')
    arquivo.write(dados)
    arquivo.close()


def novo_celular():
    print('Criando novo celular...\n')
    
    # obter dados
    nome = input('Nome: ')
    marca = input('Marca: ')
    tela = input('Tela("): ')
    valor = float(input('valor(R$): '))
    cam_frontal = input('Camera frontal (sim/nao): ')

    # inserindo no dicionario
    celular = {}
    celular['nome'] = nome
    celular['marca'] = marca
    celular['tela'] = tela
    celular['valor'] = valor
    celular['cam_frontal'] = cam_frontal

    return celular


def mostra_celulares(celulares):
    qtd = len(celulares)
    print(f'listando {qtd} celulares\n')

    for celular in celulares:
        print('Nome:', celular['nome'])
        print('Marca:', celular['marca'])
        print('Tela("):', celular['tela'])
        print('Valor(R$):', celular['valor'])
        print('Camera frontal:', celular['cam_frontal'])
        print('-'*30)
        

def encontra_celular(buscador, celulares):
    lista = []
    
    busca1 = buscador.upper()
    codigo = 0

    for celular in celulares:
        if busca1 in celular['nome'].upper():
            codigo += 1
            lista.append([codigo, celular['nome'], celular['marca']])
        
        elif busca1 in celular['marca'].upper():
            codigo += 1
            lista.append([codigo, celular['nome'], celular['marca']])

    return lista


def mostra_resultados_pesquisa(lista):
    print(f'\nForam encontrados {len(lista)} celulares\n')

    if len(lista) > 0:
        for item in lista:
            print('Código:', item[0])
            print('Nome:', item[1])
            print('Marca:', item[2])
            print('-'*30)
    else:
        main()


def encontra_celular_especifico(buscador, celulares):
    cod = int(input('Digite o código do celular que deseja acessar: '))
    lista = encontra_celular(buscador, celulares)

    if cod >= 1 and cod <= len(lista):
        for celular in celulares:
            if (lista[cod-1][1] == celular['nome']) and (lista[cod-1][2] == celular['marca']):
                return celular
    else:
        print('\nCódigo inválido!')
        return False


def tela_especifica():
    menu = '\n***** Menu de Acesso Específico *****\n'
    menu += '1 - Mostrar detalhes do celular\n'
    menu += '2 - Remover celular\n'
    menu += '3 - Editar celular\n'
    menu += '4 - Duplicar registro do celular\n'
    menu += '0 - Voltar ao menu inicial\n'
    menu += '\nOpção >>> '

    return menu


def main2(nome_arquivo, celulares, buscador):
    menu = tela_especifica()
    celular_especifico = encontra_celular_especifico(buscador, celulares)

    if celular_especifico != False:
        opcao = int(input(menu))

        while opcao != 0:
            if opcao == 1:
                mostra_detalhes(celular_especifico, celulares)

            elif opcao == 2:
                remove_celular(nome_arquivo, celular_especifico, celulares)
                
            elif opcao == 3:
                edita_celular(nome_arquivo, celular_especifico, celulares)
                
            elif opcao == 4:
                duplica_celular(nome_arquivo, celular_especifico, celulares)
            
            input('<enter> to continue...\n')
            opcao = int(input(menu))
    

def mostra_detalhes(celular_especifico, celulares):
    for celular in celulares:
        if celular_especifico == celular:
            print('\nNome:', celular['nome'])
            print('Marca:', celular['marca'])
            print('Tela("):', celular['tela'])
            print('Valor(R$):', celular['valor'])
            print('Camera frontal:', celular['cam_frontal'])
            print()


def remove_celular(nome_arquivo, celular_especifico, celulares):
    for celular in celulares:
        if celular_especifico == celular:
            celulares.remove(celular)

            dados = json.dumps(celulares)
            arquivo = open(nome_arquivo, 'w')
            arquivo.write(dados)
            arquivo.close()

            print('Celular removido da lista com sucesso!')
            break


def edita_celular(nome_arquivo, celular_especifico, celulares):
    menu = tela_edicao()

    for celular in celulares:
        if celular_especifico == celular:
            opcao = int(input(menu))
            
            while opcao != 0:
                if opcao == 1:
                    print(f"Nome atual: {celular['nome']}")
                    novo_nome = input('Digite o novo nome: ')
                    celular['nome'] = novo_nome
                    
                elif opcao == 2:
                    print(f"Marca atual: {celular['marca']}")
                    nova_marca = input('Digite a nova marca: ')
                    celular['marca'] = nova_marca
                    
                elif opcao == 3:
                    print(f'Tela atual("): {celular["tela"]}')
                    nova_tela = input('Digite  a nova tela: ')
                    celular['tela'] = nova_tela
                    
                elif opcao == 4:
                    print(f"Valor atual(R$): {celular['valor']}")
                    novo_valor = input('Digite o novo valor: ')
                    celular['valor'] = novo_valor

                elif opcao == 5:
                    print(f"Status atual (câmera frontal ): {celular['cam_frontal']}")
                    nova_cam_frontal = input('Digite a nova câmera frontal (sim/nao): ')
                    celular['cam_frontal'] = nova_cam_frontal
                
                print('\nEdição realizada com sucesso!')
                input('<enter> to continue...\n')
                opcao = int(input(menu))

            dados = json.dumps(celulares)
            arquivo = open(nome_arquivo, 'w')
            arquivo.write(dados)
            arquivo.close()


def duplica_celular(nome_arquivo, celular_especifico, celulares):
    for celular in celulares:
        if celular_especifico == celular:
            celulares.append(celular)

            dados = json.dumps(celulares)
            arquivo = open(nome_arquivo, 'w')
            arquivo.write(dados)
            arquivo.close()
            
            print('Registro do celular duplicado com sucesso!')
            break


def tela_edicao():
    menu = '\n***** Menu de Edição *****\n'
    menu += '1 - Editar nome do celular\n'
    menu += '2 - Editar marca\n'
    menu += '3 - Editar tela\n'
    menu += '4 - Editar valor\n'
    menu += '5 - Editar câmera frontal\n'
    menu += '0 - Voltar ao menu inicial\n'
    menu += '\nOpção >>> '

    return menu


main()
