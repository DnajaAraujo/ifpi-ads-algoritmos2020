def main():
    numero = float(input("Digite um número:"))

    numero_verificado = verifica_numero(numero)
    print(numero_verificado)


def verifica_numero(n):
    novo_numero = n * 10
    
    centena = novo_numero // 100
    resto = novo_numero % 100

    dezena = resto // 10
    unidade = resto % 10

    if unidade != 0:
        return f"{n} é um número decimal."
    else:
        return f"{n:.0f} é um número inteiro."


main()