def main():
    num = int(input("Numero 1: "))

    print(verificar_numero(num))


def verificar_numero(num):
    dezena = num // 10
    unidade = num % 10

    if dezena == unidade:
        return "Dígitos iguais"
    else:
        return "Dígitos diferentes"


main()