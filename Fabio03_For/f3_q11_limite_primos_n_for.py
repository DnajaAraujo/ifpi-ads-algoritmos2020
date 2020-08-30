def main():
    limite_inferior = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: '))

    mostra_primos(limite_inferior, limite_superior)


def mostra_primos(limite_inferior, limite_superior):

    for i in range(limite_inferior, limite_superior + 1):
        if verifica_primo(i):
                print(i)
 

def verifica_primo(numero):
    conta_divisores = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            conta_divisores += 1

    if conta_divisores == 2:
        return True
    else:
        return False


main()