def main():
    quant_horas1 = float(input("Digite a quantidade de horas-aula trabalhadas pelo primeiro professor: "))
    valor_hora1 = float(input("Digite o valor por hora recebido por ele: R$ "))
    quant_horas2 = float(input("Digite a quantidade de horas-aula trabalhadas pelo segundo professor: "))
    valor_hora2 = float(input("Digite o valor por hora recebido por ele: R$ "))

    salario_maior = verifica_maior_salario(quant_horas1, valor_hora1, quant_horas2, valor_hora2)
    print(salario_maior)


def verifica_maior_salario(q1, v1, q2, v2):
    salario1 = q1 * v1
    salario2 = q2 * v2
    if salario1 > salario2:
        return "O primeiro professor tem maior salário que o segundo."
    elif salario1 < salario2:
        return "O segundo professor tem maior salário que o primeiro."
    else:
        return "Os dois professores têm salários iguais."



main()
