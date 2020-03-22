def main():
    tipo_combustivel = input("Digite o tipo de combustível (A para álcool ou G para gasolina): ")
    quant_litros = float(input("Digite a quantidade de litros: "))

    preco_combustivel = calcula_preco_combustivel(tipo_combustivel, quant_litros)
    print(preco_combustivel)


def calcula_preco_combustivel(t, q):
    if t == "A" or t == "a":
        if q <= 20:
            preco = 1.90
            percentual = 0.03
            preco_total = (preco * q) - (q * (preco * percentual))

        else:
            preco = 1.90
            percentual = 0.05
            preco_total = (preco * q) - (q * (preco * percentual))
    
        return f"O preço a ser pago é igual a R$ {preco_total:.2f}"

    elif t == "G" or t == "g":
        if q <= 20:
            preco = 2.50
            percentual = 0.05
            preco_total = (preco * q) - (q * (preco * percentual))

        else:
            preco = 2.50
            percentual = 0.06
            preco_total = (preco * q) - (q * (preco * percentual))

        return f"O preço a ser pago é igual a R$ {preco_total:.2f}"
    
    else:
        return "Tipo de combustível inválido!"


main()



