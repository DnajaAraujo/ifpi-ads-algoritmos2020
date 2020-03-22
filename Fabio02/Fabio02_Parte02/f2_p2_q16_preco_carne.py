def main():
    tipo_carne = input("Digite o tipo de carne (F para Filé, A para alcatra ou P para picanha): ")
    quant_carne = float(input("Digite a quantidade em Kg de carne que deseja: "))
    tipo_pagamento = input("Digite o tipo de pagamento (C para cartão ou D para dinheiro): ")

    preco_carne = calcula_preco_carne(tipo_carne, quant_carne, tipo_pagamento)
    print(preco_carne)


def calcula_preco_carne(t, q, tp):
    if t == "F" or t == "f":
        t = "Filé"
        if q <= 5:
            preco_total = q * 4.90
        else:
            preco_total = q * 5.80
        
    elif t == "A" or t == "a":
        t = "Alcatra"
        if q <= 5:
            preco_total = q * 5.90
        else:
            preco_total = q * 6.80

    elif t == "P" or t == "p":
        t = "Picanha"
        if q <= 5:
            preco_total = q * 6.90
        else:
            preco_total = q * 7.80

    else:
        return "Tipo de carne inválido!"
    

    if tp == "C" or tp == "c":
            tp = "Cartão"
            desconto = preco_total * 0.05
            valor_pagar = preco_total - desconto
    elif tp == "D" or tp == "d":
            tp = "Dinheiro"
            desconto = 0
            valor_pagar = preco_total - desconto
    else:
            return "Tipo de pagamento inválido!"

    titulo = "---- Mercado ----\n"
    a = f"fTipo de carne: {t}\n"
    b = f"Quantidade: {q}Kg\n"
    c = f"Preço total: R$ {preco_total:.2f}\n"
    d = f"Tipo de pagamento: {tp}\n"
    e = f"Valor do desconto: R$ {desconto:.2f}\n"
    f = f"Valor a pagar: R$ {valor_pagar:.2f}\n"
    rodape = "-----------------"

    return f"{titulo}{a}{b}{c}{d}{e}{f}{rodape}"


main()