def main():
    numero1 = int(input("Digite um número inteiro: "))
    numero2 = int(input("Digite um outro número inteiro: "))
    numero3 = int(input("Digite um outro número inteiro: "))

    ordem = ordenar_numeros(numero1, numero2, numero3)
    print(ordem)


def maior_numero(n1, n2, n3):
    maior = n1

    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    return maior
    

def menor_numero(n1, n2, n3):
    menor = n1

    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    return menor


def numero_meio(n1, n2, n3):
    a = menor_numero(n1, n2, n3)
    b = maior_numero(n1, n2, n3)

    if (a == n1 and b == n3) or (a == n3 and b == n1):
        return n2
    if (a == n1 and b == n2) or (a == n2 and b == n1):
        return n3
    if (a == n2 and b == n3) or (a == n3 and b == n2):
        return n1


def ordenar_numeros(n1, n2, n3):
    primeiro = menor_numero(n1, n2, n3)
    segundo = numero_meio(n1, n2, n3)
    terceiro = maior_numero(n1, n2, n3)

    return f"{primeiro}, {segundo}, {terceiro}"


main()


    

