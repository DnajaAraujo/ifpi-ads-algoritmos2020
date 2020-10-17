def main():
    qtd_elementos = int(input(">> Quantos elementos deseja adicionar ao vetor? "))
    vetor = cria_vetor(qtd_elementos)

    mostra_resultado(vetor)


def cria_vetor(qtd_elementos):
    vetor = []

    for i in range(qtd_elementos):
        elemento = int(input('Digite um número: '))
        vetor.append(elemento)

    return vetor
    
    
def maior_numero(vetor):
    maior = vetor[0]

    for i in range(1, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]

    return maior


def menor_numero(vetor):
    menor = vetor[0]

    for i in range(1, len(vetor)):
        if vetor[i] < menor:
            menor = vetor[i]

    return menor


def encontra_posicao(vetor, numero):
    for i in range(len(vetor)):
        if vetor[i] == numero:
            posicao = i

    return posicao


def mostra_resultado(vetor):
    print()
    print(f'>> Maior elemento: {maior_numero(vetor)}')
    print(f'>> Posição: {encontra_posicao(vetor, maior_numero(vetor))}')
    print()
    print(f'>> Menor elemento: {menor_numero(vetor)}')
    print(f'>> Posição: {encontra_posicao(vetor, menor_numero(vetor))}')
    print()


if __name__ == "__main__":
    main()