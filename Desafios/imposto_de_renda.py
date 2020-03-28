def main():
    renda = float(input("Digite sua renda: R$ "))
    
    imposto_vigente = calcular_tributacao_vigente(renda)
    imposto_corrigido = calcular_tributacao_corrigida(renda)

    print("-" * 30)
    print(f"Valor do IR vigente: R$ {imposto_vigente:.2f}")
    print(f"Valor do IR corrigido: R$ {imposto_corrigido:.2f}")
    print("-" * 30)

    
def calcular_tributacao_vigente(renda):
    
    imposto = 0.0

    if renda > 4664.68:
        renda_tributar = renda - 4664.69
        renda -= renda_tributar
        imposto += renda_tributar * (27.5/100)

    if renda >= 3751.06:
        renda_tributar = renda - 3751.06
        renda -= renda_tributar
        imposto += renda_tributar * (22.5/100)

    if renda >= 2826.66:
        renda_tributar = renda - 2826.66
        renda -= renda_tributar
        imposto += renda_tributar * (15/100)

    if renda >= 1903.99:
        renda_tributar = renda - 1903.99
        renda -= renda_tributar
        imposto += renda_tributar * (7.5/100)

    
    return imposto


def calcular_tributacao_corrigida(renda):
    
    imposto = 0.0

    if renda >= 9564.42:
        renda_tributar = renda - 9564.42
        renda -= renda_tributar
        imposto += renda_tributar * (27.5/100)

    if renda >= 7654.68:
        renda_tributar = renda - 7654.68
        renda -= renda_tributar
        imposto += renda_tributar * (22.5/100)

    if renda >= 5714.12:
        renda_tributar = renda - 5714.12
        renda -= renda_tributar
        imposto += renda_tributar * (15/100)

    if renda >= 3881.66:
        renda_tributar = renda - 3881.66
        renda -= renda_tributar
        imposto += renda_tributar * (7.5/100)


    return imposto


if __name__ == "__main__":
    main()
