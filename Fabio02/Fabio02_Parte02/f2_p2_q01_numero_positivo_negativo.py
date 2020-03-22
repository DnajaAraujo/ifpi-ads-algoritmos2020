def main():
    numero = float(input("Digite um número: ")) 

    numero_analisado = analisa_numero(numero)
    print(numero_analisado)


def analisa_numero(n):
    if n < 0:
        return f"O número {n} é negativo."
    else:
        return f"O número {n} é positivo."


main()