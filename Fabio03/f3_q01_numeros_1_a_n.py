def main():
    numero = int(input('Digite um número: '))
    escreve_numeros(numero)


def escreve_numeros(n):
    contador = 1
    while True:
        if contador <= n:
            print(contador)

            contador += 1

        else:
            break  


main()
