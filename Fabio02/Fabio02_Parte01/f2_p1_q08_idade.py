def main():
    dia_atual = int(input("Digite o dia atual: "))
    mes_atual = int(input("Digite o mês atual: "))
    ano_atual = int(input("Digite o ano atual: "))

    dia_nasc = int(input("Digite o dia do seu nascimento: "))
    mes_nasc = int(input("Digite o mês do seu nascimento: "))
    ano_nasc = int(input("Digite o ano do seu nascimento: "))

    idade = verifica_data(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nasc, ano_nasc)
    print(idade)


def calcula_idade(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nasc, ano_nasc):
    idade_parcial = ano_atual - ano_nasc
    if dia_atual < dia_nasc or mes_atual < mes_nasc:
        return f"Sua idade atual é igual é {idade_parcial - 1} anos."
    else:
        return f"Sua idade atual é igual é {idade_parcial} anos."


def verifica_data(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nasc, ano_nasc):
    if (dia_atual == 30) and (mes_atual == 2) or (dia_nasc == 30) and (mes_nasc == 2):
        return "Data inválida!"
    if ((dia_atual <= 0 or dia_atual > 30) or (mes_atual <= 0 or mes_atual > 12) or ano_atual <= 0):
        return "Data inválida!"
    elif ((dia_nasc <= 0 or dia_nasc > 30) or (mes_nasc <= 0 or mes_nasc > 12) or ano_nasc <= 0):
        return "Data inválida!"
    else:
        return calcula_idade(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nasc, ano_nasc)


main()