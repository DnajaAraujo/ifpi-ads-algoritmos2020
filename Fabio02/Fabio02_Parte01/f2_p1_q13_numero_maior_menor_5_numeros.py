def main():
    numero1 = int(input("Digite um número inteiro: "))
    numero2 = int(input("Digite um outro número inteiro: "))
    numero3 = int(input("Digite um outro número inteiro: "))
    numero4 = int(input("Digite um outro número inteiro: "))
    numero5 = int(input("Digite um outro número inteiro: "))

    retorno = retorna_maior_menor(numero1, numero2, numero3, numero4, numero5)
    print(retorno)


def maior_numero(n1, n2, n3, n4, n5):
    maior = n1

    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    if n4 > maior:
        maior = n4
    if n5 > maior:
        maior = n5 
    return maior
    

def menor_numero(n1, n2, n3, n4, n5):
    menor = n1

    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    if n4 < menor:
        menor = n4
    if n5 < menor:
        menor = n5
    return menor


def retorna_maior_menor(n1, n2, n3, n4, n5):
    a = menor_numero(n1, n2, n3, n4, n5)
    b = maior_numero(n1, n2, n3, n4, n5)

    return f"O menor número digitado é {a} e o maior número digitado é {b}"


main()