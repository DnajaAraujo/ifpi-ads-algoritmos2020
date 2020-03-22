def main():
    pergunta1 = input("Telefonou para a vítima? (S para Sim ou N para Não): ")
    pergunta2 = input("Esteve no local no crime? (S para Sim ou N para Não): ")
    pergunta3 = input("Mora perto da vítima? (S para Sim ou N para Não): ")
    pergunta4 = input("Devia para a vítima? (S para Sim ou N para Não): ")
    pergunta5 = input("Já trabalhou com a vítima? (S para Sim ou N para Não): ")

    print("----------------------------------------------------")
    participacao = analisa_participacao(pergunta1, pergunta2, pergunta3, pergunta4, pergunta5)
    print(participacao)


def analisa_participacao(p1, p2, p3, p4, p5):
    respostas_positivas = 0

    if p1 == "S" or p1 == "s":
        respostas_positivas += 1
    if p2 == "S" or p2 == "s":
        respostas_positivas += 1
    if p3 == "S" or p3 == "s":
        respostas_positivas += 1
    if p4 == "S" or p4 == "s":
        respostas_positivas += 1
    if p5 == "S" or p5 == "s":
        respostas_positivas += 1
     
    if respostas_positivas == 2:
        return "Suspeito."
    elif respostas_positivas == 3 or respostas_positivas == 4:
        return "Cúmplice."
    elif respostas_positivas == 5:
        return "Assassino."
    else:
        return "Inocente."
    
    
main()