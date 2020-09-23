def palavras_tres_letras_duplas():
    print('>> Car Talk: Palavras com 3 letras duplas \n')
    arquivo = open('words.txt')
    
    for linha in arquivo:
        palavra = linha.strip()
        if verifica_tres_letras_duplas(palavra):
            print(palavra)
    
    arquivo.close()


def verifica_tres_letras_duplas(palavra):
    i = 0
    contador = 0

    while i < len(palavra) - 1:
        if palavra[i] == palavra[i+1]:
            contador += 1
            if contador == 3:
                return True
            i += 2
        else:
            i = i + 1 - (2 * contador)
            contador = 0
    return False

    



