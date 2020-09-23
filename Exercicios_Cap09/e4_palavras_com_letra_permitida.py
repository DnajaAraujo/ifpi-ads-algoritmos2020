def palavras_com_letra_permitida():
    print('>> Palavras com letras permitidas \n')
    arquivo = open('words.txt')

    letras_permitidas = input('Digite as letras que deseja permitir: ')

    for linha in arquivo:
        palavra = linha.strip()
        if uses_only(palavra, letras_permitidas):
            print(palavra)

    arquivo.close()


def uses_only(palavra, letras_permitidas):
    for letra in palavra:
        if letra not in letras_permitidas:
            return False

    return True

