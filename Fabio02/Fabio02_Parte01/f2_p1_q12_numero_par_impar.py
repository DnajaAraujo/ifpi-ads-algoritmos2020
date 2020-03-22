def main():
    numero = int(input("Digite um número inteiro: "))
    
    numero_verificado = verifica_numero(numero)
    print(numero_verificado)


def verifica_numero(n):
    if n % 2 == 0:
        return f"{n} é um número par"
    else:
        return f"{n} é um número ímpar"


main()