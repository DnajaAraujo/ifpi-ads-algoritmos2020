def main():
    altura = float(input("Digite sua altura em metros (m): "))
    peso = float(input("Digite seu peso em quilogramas (Kg): "))

    imc_calculado = calcula_imc(altura, peso)
    print(imc_calculado)


def calcula_imc(a, p):
    imc = (p / (a ** 2))
    if imc < 25:
        return "Você está normal."
    elif imc >= 25 and imc <= 30:
        return "Você está obeso."
    else:
        return "Você está obeso mórbido."


main()
