def main():
    numero = int(input('Digite um número: '))
    calcula_s(numero)


def calcula_s(numero):
    contador = 1
    resultado = 0

    while contador <= numero:
        if numero == 1:
            resultado += numero / 1
            break
        
        elif contador % 2 == 0:
            numerador = numero - (contador - 1)
            denominador = contador
            fracao = - (numerador / denominador)

        elif contador % 2 != 0:
            denominador = numero - (contador - 1)
            numerador = contador
            fracao = numerador / denominador

        resultado += fracao
        contador += 1
        
    print('resultado: {}'.format(resultado))


main()
