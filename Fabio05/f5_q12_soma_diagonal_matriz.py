from matriz_funcoes import *

def main():
    ordem = int(input('>> Deseja uma matriz de qual ordem? '))
    matriz = cria_matriz_quadrada(ordem)

    mostra_resultado(ordem, matriz)


def soma_diagonal_principal(matriz):
    diagonal_principal = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                diagonal_principal += matriz[i][j]
    
    return diagonal_principal


def soma_diagonal_secundaria(ordem, matriz):
    diagonal_secundaria = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (i+1) + (j+1) == ordem + 1:
                diagonal_secundaria += matriz[i][j]

    return diagonal_secundaria


def soma_nao_diagonal(ordem, matriz):
    nao_diagonal = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if ((i+1) + (j+1) != ordem + 1) and (i != j):
                nao_diagonal += matriz[i][j]

    return nao_diagonal


def mostra_resultado(ordem, matriz):
    mostra_matriz(matriz)
    print(f'>> Soma da diagonal principal: {soma_diagonal_principal(matriz)}')
    print(f'>> Soma da diagonal secundária: {soma_diagonal_secundaria(ordem, matriz)}')
    print(f'>> Soma dos elementos não diagonais: {soma_nao_diagonal(ordem, matriz)}')
    print()


if __name__ == "__main__":
    main()