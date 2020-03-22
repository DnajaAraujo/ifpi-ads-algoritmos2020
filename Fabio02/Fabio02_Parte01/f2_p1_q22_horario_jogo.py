def main():
    hora_inicio = int(input("Digite a hora de início do jogo: "))
    min_inicio = int(input("Digite o minuto de início do jogo: "))
    hora_termino = int(input("Digite a hora de término do jogo: "))
    min_termino = int(input("Digite o minuto de término do jogo: "))

    duração = calcula_duracao_jogo(hora_inicio, min_inicio, hora_termino, min_termino )
    print(duração)



def calcula_duracao_jogo(h1, m1, h2, m2):
    if (h1 > 23 or m1 > 59) or (h2 > 23 or m2 > 59):
        return "Horários Inválidos!"
    elif h2 < h1:
        h2 += 24
    elif (h1 == h2) and (m1 == m2):
        h2 += 24

    minutos1 = (h1 * 60) + m1
    minutos2 = (h2 * 60) + m2
    horas_totais = (minutos2 - minutos1) // 60
    minutos_totais = (minutos2 - minutos1) % 60

    if horas_totais > 24:
        return "Erro: Esse jogo superou as 24 horas de duração!"
    else:
        return f"Esse jogo durou {horas_totais} hora(s) e {minutos_totais} minuto(s)."



main()










