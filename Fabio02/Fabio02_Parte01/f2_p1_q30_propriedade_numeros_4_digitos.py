def main():
    numero = int(input("Digite um número inteiro de 4 dígitos: "))

    quadrado_perfeito = retorna_quadrado_perfeito(numero)
    print(quadrado_perfeito)


def retorna_quadrado_perfeito(n):
    if len(str(n)) > 4:
        return "Erro: Número com mais de 4 dígitos."
    elif len(str(n)) < 4:
        return "Erro: Número com menos de 4 dígitos."
        
    milhar = n // 1000
    resto = n % 1000 

    centena = resto // 100
    resto = resto % 100

    dezena = resto // 10
    unidade = resto % 10

    dezena_util1 = (milhar * 10) + centena
    dezena_util2 = (dezena * 10) + unidade
    soma_dezena = dezena_util1 + dezena_util2

    if (soma_dezena ** 2) == n:
        return f"O número {n} atende a propriedade.\n{n} -> {dezena_util1} + {dezena_util2} = {soma_dezena} -> {soma_dezena}^2 = {n}"
    else:
        return f"O número {n} não atende a propriedade.\n{n} -> {dezena_util1} + {dezena_util2} = {soma_dezena} -> {soma_dezena}^2 ≠ {n}"


main()