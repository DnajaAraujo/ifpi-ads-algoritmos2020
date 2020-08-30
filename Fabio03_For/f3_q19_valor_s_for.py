def main():
    numero = int(input('Digite um número: '))
    calcula_s(numero)


def calcula_s(numero):
    resultado = 0

    for i in range(1, numero + 1):
        if numero == 1:
            resultado += numero / 1
            break
        
        elif i % 2 == 0:
            numerador = numero - (i - 1)
            denominador = i
            fracao = - (numerador / denominador)

        elif i % 2 != 0:
            denominador = numero - (i - 1)
            numerador = i
            fracao = numerador / denominador

        resultado += fracao
        
    print('resultado: {}'.format(resultado))


main()