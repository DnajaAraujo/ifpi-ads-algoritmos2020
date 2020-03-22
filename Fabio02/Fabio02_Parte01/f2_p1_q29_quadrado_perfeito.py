def main():
    numero = int(input("Digite um número inteiro de 4 dígitos: "))

    quadrado_perfeito = retorna_quadrado_perfeito(numero)
    print(quadrado_perfeito)


def retorna_quadrado_perfeito(n):
    milhar = n // 1000
    resto = n % 1000 

    centena = resto // 100
    resto = resto % 100

    dezena = resto // 10
    unidade = resto % 10

    dezena_util1 = (milhar * 10) + centena
    dezena_util2 = (dezena * 10) + unidade
    soma_dezena = dezena_util1 + dezena_util2

    if (n**0.5) == soma_dezena:
        return f"O número {n} é um quadrado perfeito."
    else:
        return f"O número {n} não é um quadrado perfeito."


main()