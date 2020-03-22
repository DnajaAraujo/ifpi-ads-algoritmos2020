def main():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    print("-------------------------------------------------")
    situacao_avaliada = avalia_situacao_aluno(nota1, nota2)
    print(situacao_avaliada)
    print("-------------------------------------------------")


def avalia_situacao_aluno(n1, n2):
    media = (n1 + n2) / 2

    if media > 9 and media <= 10:
        conceito = "A"
    elif media > 7.5 and media <= 9:
        conceito = "B"
    elif media > 6 and media <= 7.5:
        conceito = "C"
    elif media > 4 and media <= 6:
        conceito = "D"
    elif media >= 0 and media <=4:
        conceito = "E"

    if conceito == "A" or conceito == "B" or conceito == "C":
        situacao = "Aprovado."
    else:
        situacao ="Reprovado."
    
    return f"Notas: {n1} e {n2}\nMédia: {media}\nConceito: {conceito}\nSituação: {situacao}"


main()
    