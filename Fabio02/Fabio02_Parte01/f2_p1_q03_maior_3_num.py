def main():
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    num3 = int(input("Numero 3: "))

    maior = verificar_maior(num1, num2, num3)

    print(maior)


def verificar_maior(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return f"O {num1} é o maior"

    elif num2 > num1 and num2 > num3:
        return f"O {num2} é o maior"

    elif num3 > num1 and num3 > num2:
        return f"O {num3} é o maior"

    elif num1 == num2 and num1 != num3:
        return f"O {num1} é o maior"

    elif num1 == num3 and num1 != num2:
        return f"O {num3} é o maior"

    elif num2 == num3 and num2 != num1:
        return f"O {num3} é o maior"

    else:
        return "Números iguais"


main()