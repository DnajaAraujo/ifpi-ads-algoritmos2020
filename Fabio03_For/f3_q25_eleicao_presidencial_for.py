def main():
    numero_eleitores = int(input('Digite o número de eleitores: '))
    conta_votos(numero_eleitores)


def conta_votos(numero_eleitores):
    candidato1 = 0
    candidato2 = 0
    candidato3 = 0
    votos_nulos = 0
    votos_branco = 0

    for i in range(1, numero_eleitores + 1):
        voto = int(input('Digite o número do voto: '))

        if voto == 1:
            candidato1 += 1
        elif voto == 2:
            candidato2 += 1
        elif voto == 3:
            candidato3 += 1
        elif voto == 9:
            votos_nulos += 1
        elif voto == 0:
            votos_branco += 1


    print('-'*30)
    print('1° Candidado: ', candidato1)
    print('2° Candidado: ', candidato2)
    print('3° Candidado: ', candidato3)
    print('Votos nulos: ', votos_nulos)
    print('Votos em branco: ', votos_branco)
    print('-'*30)

    venceu_eleicao(candidato1, candidato2, candidato3)


def venceu_eleicao(c1, c2, c3):
    vencedor = c1

    if c2 > vencedor:
        vencedor = c2
    if c3 > vencedor:
        vencedor = c3

    if (vencedor == c1) and (vencedor != c2) and (vencedor != c3):
        print('O 1° candidato venceu.')
    elif (vencedor == c2) and (vencedor != c1) and (vencedor != c3):
        print('O 2° candidato venceu.')
    elif (vencedor == c3) and (vencedor != c1) and (vencedor != c2):
        print('O 3° candidato venceu.')
    else:
        print('Nenhum candidato venceu.')
    
    print('-'*30)


main()