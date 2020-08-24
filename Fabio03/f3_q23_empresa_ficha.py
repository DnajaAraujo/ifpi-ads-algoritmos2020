def main():
    numero_ficha = int(input('Digite o número de fichas desejadas: '))
    preenche_ficha(numero_ficha)


def preenche_ficha(numero_ficha):
    contador = 1

    while contador <= numero_ficha:
        codigo = int(input('Digite o código do funcionário: '))
        horas_trabalho = float(input('Digite o número de horas trabalhadas: '))
        numero_dependentes = int(input('Digite o número de dependentes: '))

        contador += 1

        calcula_valores(horas_trabalho, numero_dependentes)


def calcula_valores(horas_trabalho, numero_dependentes):
    salario_bruto = (12 * horas_trabalho) + (40 * numero_dependentes)
    desconto_inss = salario_bruto * (8.5/100)
    desconto_ir = salario_bruto * (5/100)
    salario_liquido = salario_bruto - (desconto_inss + desconto_ir)

    mostra_valores(salario_bruto, desconto_inss, desconto_ir, salario_liquido)


def mostra_valores(salario_bruto, desconto_inss, desconto_ir, salario_liquido):
    print('-'*30)
    print('Descontos INSS: R$ {:.2f}'.format(desconto_inss))
    print('Descontos IR: R$ {:.2f}'.format(desconto_ir))
    print('Salário líquido: R$ {:.2f}'.format(salario_liquido))
    print('-'*30)


main()