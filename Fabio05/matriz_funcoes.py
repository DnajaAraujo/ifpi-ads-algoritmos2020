def cria_matriz_quadrada(ordem):
    matriz = []
    for i in range(ordem):
        matriz.append([])

    for i in range(ordem):
        print(f'\n-- {i+1}° Linha --')

        for j in range(ordem):
            item = int(input('>> Digite um número: '))
            matriz[i].append(item)
    
    print()
    return matriz


def mostra_matriz(matriz):
    print()
    for item in matriz:
        print(item)
        
    print()
       