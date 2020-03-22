def main():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    situacao = avalia_situacao_aluno(nota1, nota2)
    print(situacao)


def avalia_situacao_aluno(n1, n2):
    media = (n1 + n2) / 2

    if media >= 7 and media != 10:
        return "Situação do aluno: Aprovado."
    elif media == 10:
        return "Situação do aluno: Aprovado com distinção."
    else:
        return "Situação do aluno: Reprovado."


main()