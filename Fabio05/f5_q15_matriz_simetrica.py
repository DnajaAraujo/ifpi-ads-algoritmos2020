from matriz_funcoes import *

def main():
    ordem = int(input('>> Deseja uma matriz de qual ordem? '))
    matriz = cria_matriz_quadrada(ordem)

    mostra_resultado(matriz)


def verifica_simetria(matriz):
    itens_totais = 0
    simetricos = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            itens_totais += 1

            if matriz[i][j] == matriz[j][i]:
                simetricos += 1
    
    return simetricos == itens_totais

    
def mostra_resultado(matriz):
    if verifica_simetria(matriz):
        print('>> Esta matriz é simétrica!')
    else:
        print('>> Esta matriz não é simétrica!')
    
    mostra_matriz(matriz)


if __name__ == "__main__":
    main()