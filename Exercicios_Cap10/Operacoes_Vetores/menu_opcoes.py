from operacoes_basicas import *
from operacoes_numericas import *
from operacoes_transformacao import *

def main():
    menu = '*** Brincando com Listas ***'
    menu += '\n 1 - Inserir valores'
    menu += '\n 2 - Adicionar valor na posição'
    menu += '\n 3 - Mostrar lista'
    menu += '\n 4 - Mostrar valor pela posição'
    menu += '\n 5 - Substituir valor'
    menu +='\n'
    menu += '\n 6 - Remover do início'
    menu += '\n 7 - Remover do final'
    menu += '\n 8 - Remover de posição específica'
    menu += '\n 9 - Organizar lista'
    menu += '\n 10 - Inverter lista'
    menu +='\n'
    menu += '\n 11 - Mostrar quantidade de números pares'
    menu += '\n 12 - Mostrar quantidade de números ímpares'
    menu += '\n 13 - Mostrar quantidade de números primos'
    menu += '\n 14 - Mostrar quantidade de números zero'
    menu += '\n 15 - Mostrar quantidade de números positivos'
    menu += '\n'
    menu += '\n 16 - Mostrar quantidade de números negativos'
    menu += '\n 17 - Mostrar ocorrências de um valor'
    menu += '\n 18 - Mostrar média dos números'
    menu += '\n 19 - Dobrar todos os valores'
    menu += '\n 20 - Dobrar todos os multiplos de um valor'
    menu += '\n'
    menu += '\n 21 - Dobrar todos os divisores de um valor'
    menu += '\n 22 - Multiplicar toda lista por um valor'
    menu += '\n 23 - Dividir toda lista por um valor'
    menu += '\n 24 - Apagar lista'
    menu += '\n 0 - Sair'
    menu += '\n'
    menu += '\n Opção >>> '

    lista = []

    while True:  # Condição sempre verdadeira, só irá para em caso de break ou error
        opcao = int(input(menu))
        print()

        if opcao == 1:
            insere_valores(lista)
        elif opcao == 2:
            adiciona_valor_posicao(lista)
        elif opcao == 3:
            mostra_lista(lista)
        elif opcao == 4:
            mostra_valor(lista)
        elif opcao == 5:
            substitui_valor_posicao(lista)
            
        elif opcao == 6:
            remove_inicio(lista)
        elif opcao == 7:
            remove_final(lista)
        elif opcao == 8:
            remove_posicao_especifica(lista)
        elif opcao == 9:
            organiza_lista(lista)
        elif opcao == 10:
            inverte_lista(lista)

        elif opcao == 11:
            conta_pares(lista)
        elif opcao == 12:
            conta_impares(lista)
        elif opcao == 13:
            conta_primos(lista)
        elif opcao == 14:
            conta_zero(lista)
        elif opcao == 15:
            conta_positivos(lista)
        elif opcao == 16:
            conta_negativos(lista)
        elif opcao == 17:
            conta_ocorrencia_valor(lista)

        elif opcao == 18:
            calcula_media(lista)
        elif opcao == 19:
            dobra_valores(lista)
        elif opcao == 20:
            dobra_multiplos(lista)
        elif opcao == 21:
            dobra_divisores(lista)
        elif opcao == 22:
            multiplica_valores(lista)
        elif opcao == 23:
            divide_valores(lista)
        elif opcao == 24:
            apaga_valores(lista)
        elif opcao == 0:
            break
        else:
            print('Opção Inválida')

        input('<enter> to continue...\n')


main()