def main():
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))

    maior = verificar_maior(num1, num2)

    print(maior)


def verificar_maior(num1, num2):
    if num1 > num2:
        return f"O número {num1} é maior que o {num2}"
    elif num2 > num1:
        return f"O número {num2} é maior que o {num1}"
    else:
        return "Números iguais"


main()