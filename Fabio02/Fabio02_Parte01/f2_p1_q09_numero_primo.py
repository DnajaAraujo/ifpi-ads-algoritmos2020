def main():
    numero = int(input("Digite um número entre 0 e 100: "))

    numero_primo = verifica_numero_primo(numero)
    print(numero_primo)


def verifica_numero_primo(n):
    if (n == 1) or (n != 2 and n % 2 == 0) or (n != 3 and n % 3 == 0) or (n != 5 and n % 5 == 0) or (n != 7 and n % 7 == 0):
        return f"{n} não é um número primo."
    else:
        return f"{n} é um número primo."


main()

