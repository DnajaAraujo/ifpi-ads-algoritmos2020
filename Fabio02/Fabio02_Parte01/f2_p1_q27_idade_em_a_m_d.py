def main():
    dia_nasc = int(input("Digite o dia do seu nascimento: "))
    mes_nasc = int(input("Digite o mês do seu nascimento: "))
    ano_nasc = int(input("Digite o ano do seu nascimento: "))
    dia_atual = int(input("Digite o dia atual: "))
    mes_atual = int(input("Digite o mês atual: "))
    ano_atual = int(input("Digite o ano atual: "))

    idade = verifica_data(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nasc, ano_nasc)
    print(idade)



def calcula_idade(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nasc, ano_nasc):
    quant_dia_nasc = (ano_nasc * 365) + (mes_nasc * 30) + dia_nasc
    quant_dia_atual = (ano_atual * 365) + (mes_atual * 30) + dia_atual

    quant_dia_totais = quant_dia_atual - quant_dia_nasc
    ano_idade = quant_dia_totais // 365
    resto = quant_dia_totais % 365
    mes_idade = resto // 30
    dia_idade = resto % 30

    return f"Você tem {ano_idade} ano(s), {mes_idade} mes(es) e {dia_idade} dia(s)."



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