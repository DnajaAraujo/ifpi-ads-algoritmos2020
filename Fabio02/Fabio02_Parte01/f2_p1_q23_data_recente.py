def main():
    dia1 = int(input("Digite o dia: "))
    mes1 = int(input("Digite o mês: "))
    ano1 = int(input("Digite o ano: "))

    dia2 = int(input("Digite outro dia: "))
    mes2 = int(input("Digite outro mês: "))
    ano2 = int(input("Digite outro ano: "))

    data_recente = verifica_data(dia1, mes1, ano1, dia2, mes2, ano2)
    print(data_recente)


def calcula_data_recente(d1, m1, a1, d2, m2, a2):
    if (a1 > a2):
        return "A primeira data digitada é mais recente que a segunda."
    elif (a1 < a2):
        return "A segunda data digitada é mais recente que a primeira."
    else:
        if (m1 > m2):
            return "A primeira data digitada é mais recente que a segunda."
        if (m1 < m2):
            return "A segunda data digitada é mais recente que a primeira."
        else:
            if (d1 > d2):
                return "A primeira data digitada é mais recente que a segunda."
            elif (d1 < d2):
                return "A segunda data digitada é mais recente que a primeira."
            else:
                return "As duas datas digitadas são iguais."


def verifica_data(d1, m1, a1, d2, m2, a2):
    if ((d1 <= 0 or d1 > 30) or (m1 <= 0 or m1 > 12) or a1 <= 0):
        return "Data inválida!"
    elif ((d2 <= 0 or d2 > 30) or (m2 <= 0 or m2 > 12) or a2 <= 0):
        return "Data inválida!"
    else:
        return calcula_data_recente(d1, m1, a1, d2, m2, a2)


main()