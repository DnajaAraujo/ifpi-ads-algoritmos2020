def main():
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))

    situacao_aluno = analisa_situacao_aluno(nota1, nota2)
    print(situacao_aluno)


def analisa_situacao_aluno(n1, n2):
    media = (n1 + n2) / 2
    if media >= 7:
        return "Situação do aluno: Aprovado!"
    else:
        print(end="\n")
        print("O aluno precisa fazer o exame final.")
        exame = float(input("Digite a nota do exame final: "))
        
        media_final = (media + exame) / 2
        if media_final >= 5:
            return "Situação do aluno: Aprovado!"
        else:
            return "Situação do aluno: Reprovado!"


main()