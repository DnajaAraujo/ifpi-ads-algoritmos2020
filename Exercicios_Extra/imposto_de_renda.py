def main():
    renda = float(input("Digite sua renda em R$: "))

    tributacao_vigente = calcular_tributacao_vigente(renda)
    tributacao_corrigida = calcular_tributacao_corrigida(renda)
    imposto_vigente = renda * (tributacao_vigente / 100)
    imposto_corrigido = renda * (tributacao_corrigida / 100)

    print("------------------------------------------------------------")
    print(f"Sua Renda: R$ {renda:.2f}")
    print("------------------------------------------------------------")
    print("Porcentagem de Tributação | Valor em Reais | Estado da Tributação ")
    
    # Primeira linha
    print(f"{tributacao_vigente:.2f}%", end=" ")
    print("                    |", end=" ")
    print(f"R$ {imposto_vigente:.2f}", end=" ")
    print("       |", end=" ")
    print("Vigente")

    # Segunda linha
    print(f"{tributacao_corrigida:.2f}%", end=" ")
    print("                    |", end=" ")
    print(f"R$ {imposto_corrigido:.2f}", end=" ")
    print("       |", end=" ")
    print("Corrigida")
    print("------------------------------------------------------------")
    
    
def calcular_tributacao_vigente(renda):
    if renda <= 1903.98:
        return 0
    elif renda <= 2826.65:
        return 7.5
    elif renda <= 3751.05:
        return 15
    elif renda <= 4664.68:
        return 22.5
    else:
        return 27.5 


def calcular_tributacao_corrigida(renda):
    if renda <= 3881.65:
        return 0
    elif renda <= 5714.11:
        return 7.5
    elif renda <= 7654.67:
        return 15
    elif renda <= 9564.42:
        return 22.5
    else:
        return 27.5 



main()