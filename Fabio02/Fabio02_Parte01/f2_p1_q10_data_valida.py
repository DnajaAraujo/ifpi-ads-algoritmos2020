def main():
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))

    data_valida = verifica_data(dia, mes, ano)
    print(data_valida)


def verifica_data(d, m, a):
    if (d == 30) and (m == 2):
        return "Data inválida!"
    if  (d <= 0 or d > 30) or (m <= 0 or m > 12) or a <= 0:
        return "Data inválida!"
    else:
        return "Data válida!"


main()