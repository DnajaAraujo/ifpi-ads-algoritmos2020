def main():
    mostra_tabuada()


def mostra_tabuada():
    multiplicando = 1
    multiplicador = 0

    for i in range(110):
        resultado = multiplicando * multiplicador
        print('{} x {} = {}'.format(multiplicando, multiplicador, resultado))

        multiplicador += 1
        
        if multiplicador > 10:
            multiplicando += 1
            multiplicador = 0
            print('-'*15)


main()