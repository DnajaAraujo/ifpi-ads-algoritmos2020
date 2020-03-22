def main():
    numero = int(input("Digite um número de 1 a 7: "))

    dia_analisado = analisa_dia(numero)
    print(dia_analisado)


def analisa_dia(n):
    if n == 1:
        return "Domingo."
    elif n == 2:
        return "Segunda-feira."
    elif n == 3:
        return "Terça-feira."
    elif n == 4:
        return "Quarta-feira."
    elif n == 5:
        return "Quinta-feira."
    elif n == 6:
        return "Sexta-feira."
    elif n == 7:
        return "Sábado."
    else:
        return "Valor inválido."


main()
