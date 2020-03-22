def main():
    numero1 = float(input("Digite um número: "))
    numero2 = float(input("Digite um outro número: "))
    operacao = int(input("Digite a operação desejada (1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão): "))

    numeros_calculados = calcula_numeros(numero1, numero2, operacao)
    print(numeros_calculados)


def calcula_numeros(n1, n2, op):
    print(end="\n")
    if op == 1:
        resultado = n1 + n2
        return f"Resultado: {resultado}"
    elif op == 2:
        resultado = n1 - n2
        return f"Resultado: {resultado}"
    elif op == 3:
        resultado = n1 * n2
        return f"Resultado: {resultado}"
    elif op == 4:
        resultado = n1 / n2
        return f"Resultado: {resultado}"
    else:
        return "Operação inválida!"


main()