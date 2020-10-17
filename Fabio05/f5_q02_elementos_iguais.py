def main():
    qtd_elementos = int(input('>> Quantos elementos deseja digitar? '))
    mostra_resultado(qtd_elementos)


def verifica_elementos(qtd_elementos):
    vetor = []

    for i in range(qtd_elementos):
        elemento = input('>> Digite o que deseja adicionar ao vetor: ')
        vetor.append(elemento)

    conta_iguais = 0
    
    for i in range(len(vetor)-1):
        if vetor[i] in vetor[i+1 : len(vetor)]:
            conta_iguais += 1
    
    print()
    return conta_iguais


def mostra_resultado(qtd_elementos):
    if verifica_elementos(qtd_elementos) > 0:
        print('>> Nesse vetor existem elementos iguais.')
    else:
        print('>> Nesse vetor não existem elementos iguais.')
    
    print()


if __name__ == "__main__":
    main()