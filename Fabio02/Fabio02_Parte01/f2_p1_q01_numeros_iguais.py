def main():
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    num3 = int(input("Numero 3: "))

    numeros_iguais = verificar(num1, num2, num3)

    print(f"Existem {numeros_iguais} numeros iguais")

def verificar(num1, num2, num3):
    num_iguais = 0
    if num1 == num2 and num1 != num3:
        num_iguais += 2

    if num1 == num3 and num1 != num2:
        num_iguais += 2

    if num2 == num3 and num1 != num3:
        num_iguais += 2

    if num2 == num3 and num1 == num3 and num1 == num2:
        num_iguais += 3

    return num_iguais


main()