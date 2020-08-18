def main():
    limite_inferior = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: '))

    mostra_primos(limite_inferior, limite_superior)


def mostra_primos(li, ls):
    contador = li

    while contador <= ls:
        if verifica_primo(contador):
                print(contador)

        contador += 1  


def verifica_primo(n):
    inicio = 1
    conta_divisores = 0

    while inicio <= n:
        if n % inicio == 0:
            conta_divisores += 1

        inicio += 1
    
    if conta_divisores == 2:
        return True
    else:
        return False


main()