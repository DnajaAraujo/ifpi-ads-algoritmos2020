def main():
    salario = float(input("Digite o salário: R$ "))

    salario_aumentado = aumenta_salario(salario)
    print(salario_aumentado)


def aumenta_salario(s):
    if s <= 280:
        percentual = 20
        aumento = s * (percentual / 100)
        novo_salario = s + aumento
        
    elif s > 280 and s <= 700:
        percentual = 15
        aumento = s * (percentual / 100)
        novo_salario = s + aumento
       
    elif s > 700 and s <= 1500:
        percentual = 10 
        aumento = s * (percentual / 100)
        novo_salario = s + aumento
    else:
        percentual = 5
        aumento = s * (percentual / 100)
        novo_salario = s + aumento

    separador = "-----------------------------------\n"
    a = f"Salário antes do reajuste: R$ {s:.2f}\n"
    b = f"Percentual de aumento: {percentual}%\n"
    c = f"Valor do aumento: R$ {aumento:.2f}\n"
    d = f"Novo salário: R$ {novo_salario:.2f}\n"

    return f"{separador}{a}{b}{c}{d}{separador}"


main()