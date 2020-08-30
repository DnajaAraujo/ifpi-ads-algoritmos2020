def main():
    numero = int(input('Digite um número: '))
    calcula_raiz_quadrada_exata(numero)


def calcula_raiz_quadrada_exata(numero):
    for i in range(1, numero + 1):
        raiz = numero ** (1/2)
        
        if raiz == int(raiz):
            print('√{} = {:.0f}'.format(numero,raiz))
            break

        else:
            numero -= 1
            

main()