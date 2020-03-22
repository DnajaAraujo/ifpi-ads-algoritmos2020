def main():
    preco1 = float(input("Digite o preço do primeiro produto: R$ "))
    preco2 = float(input("Digite o preço do segundo produto: R$ "))
    preco3 = float(input("Digite o preço do terceiro produto: R$ "))

    preco_menor = analisa_menor_preco(preco1, preco2, preco3)
    print(preco_menor)



def analisa_menor_preco(p1, p2, p3):
    if p1 < p2 and p1 < p3:
        return f"O primeiro produto é o mais barato - R$ {p1:.2f}"
    elif p2 < p1 and p2 < p3:
        return f"O segundo produto é o mais barato - R$ {p2:.2f}"
    elif p3 < p1 and p3 < p2:
        return f"O terceiro produto é o mais barato - R$ {p3:.2f}" 
    elif p1 == p2 and p1 < p3:
        return f"O primeiro e o segundo produto são os mais baratos - R$ {p1:.2f}"
    elif p2 == p3 and p2 < p1:
        return f"O segundo e o terceiro produto são os mais baratos - R$ {p2:.2f}"
    elif p3 == p1 and p3 < p2:
        return f"O primeiro e o terceiro produto são os mais baratos - R$ {p3:.2f}"
    else:
        return f"Todos os produtos têm o mesmo preço - R$ {p3:.2f}"
    

    
main()