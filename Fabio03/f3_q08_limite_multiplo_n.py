def main():
    numero = int(input('Digite um número: '))
    limite_inferior = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: '))

    mostra_multiplos(numero, limite_inferior, limite_superior)


def mostra_multiplos(n, li, ls):
    contador = li

    while True:
        if n == 0:
            if li == 0:
                print(n)
            break

        elif (contador <= ls) and (n != 0):
            if contador % n == 0:
                print(contador)
            contador += 1  
        
        else:
            break


main()