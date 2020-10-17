from matriz_funcoes import *
from f5_q08_maior_menor_numero import maior_numero, menor_numero


def main():
    ordem = int(input('>> Deseja uma matriz de qual ordem? '))
    matriz = cria_matriz_quadrada(ordem)
    vetor = soma_elementos_linha(matriz)

    mostra_resultado(matriz, vetor)


def soma_elementos_linha(matriz):
    vetor_soma = []
    for i in range(len(matriz)):
        soma_itens = 0

        for j in range(len(matriz[i])):
            soma_itens += matriz[i][j]

        vetor_soma.append(soma_itens)
        
    return vetor_soma


def encontra_maior_linha(vetor):
    for i in range(len(vetor)):
        if vetor[i] == maior_numero(vetor):
            maior_linha = i + 1
    
    return maior_linha


def encontra_menor_linha(vetor):
    for i in range(len(vetor)):
        if vetor[i] == menor_numero(vetor):
            menor_linha = i + 1

    return menor_linha


def mostra_resultado(matriz, vetor):
    mostra_matriz(matriz)
    print(f'>> Linha com a maior soma de elementos: {encontra_maior_linha(vetor)}')
    print(f'>> Linha com a menor soma de elementos: {encontra_menor_linha(vetor)}')
    print()


if __name__ == "__main__":
    main()
