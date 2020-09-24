from e1_palavras_mais_de_20_letras import *
from e2_palavras_sem_e import *
from e3_palavras_sem_letra_proibida import *
from e4_palavras_com_letra_permitida import *
from e5_palavras_com_letra_obrigatoria import *
from e6_palavras_com_letra_em_ordem_alfabetica import *


def main():

    menu = '##### Wordplay #####\n' \
        + '1 - Palavras com + de 20 letras\n' \
        + '2 - Palavras sem "e"\n' \
        + '3 - Palavras sem letras proibidas\n' \
        + '4 - Palavras com letras permitidas\n' \
        + '5 - Palavras com letras obrigatorias\n' \
        + '6 - Palavras com letras em ordem alfabetica\n' \
        + '0 - Sair\n' \
        + '\nDigite uma opção: '

    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            palavras_com_mais_de_20_letras()
        elif opcao == 2:
            palavras_sem_letra_e()
            # TODO
        elif opcao == 3:
            palavras_sem_letra_proibida()
            # TODO
        elif opcao == 4:
            palavras_com_letra_permitida()
            # TODO
        elif opcao == 5:
            palavras_com_letra_obrigatoria()
            # TODO
        elif opcao == 6:
            palavras_com_letra_em_ordem_alfabetica()
            # TODO
        else:
            print('Opção Inválida!')

        input('continuar <enter> ... \n')
        opcao = int(input(menu))
        
    print('Fim do Wordplay...')


main()