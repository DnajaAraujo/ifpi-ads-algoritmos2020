def palavras_com_letra_obrigatoria():
    print('>> Palavras com letras obrigatorias \n')
    arquivo = open('words.txt')

    letras_obrigatorias = input('Digite as letras obrigatorias: ')

    for linha in arquivo:
        palavra = linha.strip()
        if uses_all(palavra, letras_obrigatorias):
            print(palavra)

    arquivo.close()


def uses_all(palavra, letras_obrigatorias):
    for letra in letras_obrigatorias:
        if letra not in palavra:
            return False

    return True