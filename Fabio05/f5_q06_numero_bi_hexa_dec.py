def main():
    vetor = cria_vetor()
    mostra_resultado(vetor)
    

def cria_vetor():
    print('>> Digite 1 ou 0 para criar um número binário <<')
    vetor = []

    for i in range(8):
        num = int(input('Digite um número: '))
        vetor.append(num)

    return vetor


def converte_binario(vetor):
    binario = ''
    
    for item in vetor:
        binario += str(item)

    return binario
    
    
def converte_decimal(binario):
    decimal = 0

    for i in range(8):
        valor = int(inverte_numero(binario)[i]) * (2**i)
        decimal += valor
    
    return decimal


def converte_hexadecimal(decimal):
    hexadecimal = ''
    num = '0123456789ABCDEF'
    
    while decimal > 0:
        hexadecimal += num[decimal % 16]
        decimal = decimal // 16
    
    return inverte_numero(hexadecimal)


def inverte_numero(num):
    num_reverso = ''

    for i in range(len(num)-1, -1, -1):
        num_reverso += num[i]

    return num_reverso


def mostra_resultado(vetor):
    binario = converte_binario(vetor)
    decimal = converte_decimal(binario)
    hexadecimal = converte_hexadecimal(decimal)

    print()
    print(f'>> Número em Binário: {binario}')
    print(f'>> Número em Decimal: {decimal}')
    print(f'>> Número em Hexadecimal: {hexadecimal}')
    print()


if __name__ == "__main__":
    main()