from e1_palavras_mais_de_20_letras import *
from e2_palavras_sem_e import *
from e3_palavras_sem_letra_proibida import *
from e4_palavras_com_letra_permitida import *
from e5_palavras_com_letra_obrigatoria import *
from e6_palavras_com_letra_em_ordem_alfabetica import *
from e7_palavras_com_3_letras_duplas import *
from e8_palindromo_hodometro import *
from e9_idade_filho import *


def main():

    menu = '##### Questões Cap. 09 #####\n' \
        + '1 - Palavras com + de 20 letras\n' \
        + '2 - Palavras sem "e"\n' \
        + '3 - Palavras sem letras proibidas\n' \
        + '4 - Palavras com letras permitidas\n' \
        + '5 - Palavras com letras obrigatorias\n' \
        + '6 - Palavras com letras em ordem alfabetica\n' \
        + '7 - Car Talk: Palavras com 3 letras duplas \n' \
        + '8 - Car Talk: Palíndromo no hodômetro \n' \
        + '9 - Car Talk: Idade do filho \n' \
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
        elif opcao == 7:
            palavras_tres_letras_duplas()
            # TODO
        elif opcao == 8:
            valida_numero()
            # TODO
        elif opcao == 9:
            envia_idade_mae()
            # TODO
        else:
            print('Opção Inválida!')

        input('continuar <enter> ... \n')
        opcao = int(input(menu))
        #
    print('Fim do menu....')


main()