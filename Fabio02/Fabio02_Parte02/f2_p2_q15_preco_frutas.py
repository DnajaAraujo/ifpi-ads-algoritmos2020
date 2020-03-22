def main():
    kg_morango = float(input("Digite a quantidade em Kg de morango: "))
    kg_maca = float(input("Digite a quantidade em Kg de maçã: "))

    preco_frutas = calcula_preco_frutas(kg_morango , kg_maca)
    print(preco_frutas)


def calcula_preco_frutas(kg_morango , kg_maca):
    if kg_morango <= 5:
        preco_morango = kg_morango * 2.50
    else:
        preco_morango = kg_morango * 2.20
    
    if kg_maca <= 5:
        preco_maca = kg_maca * 1.80
    else:
        preco_maca = kg_maca * 1.50
    
    preco_total = preco_morango + preco_maca

    if (kg_morango + kg_maca) > 8 or preco_total > 25:
        preco_total -= (preco_total * 0.10)
    
    return f"O valor total da compra das frutas é igual a R$ {preco_total:.2f}"


main()