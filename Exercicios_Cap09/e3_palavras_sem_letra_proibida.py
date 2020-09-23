def palavras_sem_letra_proibida():
    print('>> Palavras sem letras probidas \n')
    arquivo = open('words.txt')
    palavras_permitidas = 0

    letras_proibidas = input('Digite as letras que deseja proibir: ')

    for linha in arquivo:
        palavra = linha.strip()
        if avoids(palavra, letras_proibidas):
            palavras_permitidas += 1

    print(f'Palavras sem Letras Proíbidas: {palavras_permitidas}')
    arquivo.close()


def avoids(palavra, letras_proibidas):
    for letra in palavra:
        if letra in letras_proibidas:
            return False

    return True
