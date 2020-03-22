def main():
    valor_hora = float(input("Digite o valor da sua hora: R$ "))
    quant_hora = float(input("Digite a quantidade de horas trabalhadas: "))

    salarios_calculados = calcula_salarios(valor_hora, quant_hora)
    print(salarios_calculados)


def calcula_salarios(v, q):
    salario_bruto = v * q
    
    if salario_bruto <= 900:
        percentual = 0
    elif salario_bruto <= 1500:
        percentual = 5
    elif salario_bruto <= 2500:
        percentual = 10
    else:
        percentual = 20

    imposto_renda = salario_bruto * (percentual/100) 

    inss = salario_bruto * 0.10
    fgts = salario_bruto * 0.11
    descontos = imposto_renda + inss
    salario_liquido = salario_bruto - descontos

    separador ="---------------------------------\n"
    a = f"Salário bruto ({v:.2f} * {q})     : R$ {salario_bruto:.2f}\n"
    b = f"(-) IR ({percentual}%)                : R$ {imposto_renda:.2f}\n"
    c = f"(-) INSS (10%)             : R$ {inss:.2f}\n"
    d = f"FGTS (11%)                 : R$ {fgts:.2f}\n"
    e = f"Total de descontos         : R$ {descontos:.2f}\n"
    f = f"Salário líquido            : R$ {salario_liquido:.2f}\n"

    return f"{separador}{a}{b}{c}{d}{e}{f}{separador}"


main()
