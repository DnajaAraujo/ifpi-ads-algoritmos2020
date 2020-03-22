def main():
    opcao = int(input("Digite a opcao (1, 2 ou 3): "))
    numero1 = float(input("Digite um número: "))
    numero2 = float(input("Digite um outro número: "))
    numero3 = float(input("Digite um outro número: "))

    opcao_processada = processa_opcao(opcao, numero1, numero2, numero3)
    print(opcao_processada)


def processa_opcao(op, n1, n2, n3):
    if op == 1:
        return n1
    elif op == 2:
        return n2
    elif op == 3:
        return n3
    else:
        return "Opção inválida!"


main()
        