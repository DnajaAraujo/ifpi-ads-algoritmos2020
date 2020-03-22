def main():
    numero = float(input("Digite um número para ser arredondado: "))

    numero_arredondado = arredonda_numero(numero)
    print(numero_arredondado)


def arredonda_numero(n):
    novo_numero = n * 10
    
    dezena_milhar = novo_numero // 10000
    resto = novo_numero % 10000
    
    unidade_milhar = resto // 1000
    resto = resto % 1000 
    
    centena = resto // 100
    resto = resto % 100

    dezena = resto // 10
    unidade = resto % 10

    if unidade >= 5:
        novo_numero = ((dezena_milhar * 10000) + (unidade_milhar * 1000) + (centena * 100) + (dezena * 10) + 10)/10
        return novo_numero
    else:
        novo_numero = ((dezena_milhar * 10000) + (unidade_milhar * 1000) + (centena * 100) + (dezena * 10)) / 10
        return novo_numero
        

main()