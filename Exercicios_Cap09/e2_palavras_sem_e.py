def palavras_sem_letra_e():
    print('>> Palavras sem letra "e" \n')
    arquivo = open('words.txt')
    total = 0
    palavras_sem_e = 0

    for linha in arquivo:
        palavra = linha.strip()
        total += 1
        
        if has_no_e(palavra):
            palavras_sem_e += 1
            print(palavra)

    perc = (palavras_sem_e / total) * 100
    print(f'Total de Palavras: {total}')
    print(f'Palavras sem "e": {palavras_sem_e}')
    print(f'Percentual {perc} %')
    arquivo.close()


def has_no_e(palavra):
    for letra in palavra:
        if letra == 'e':
            return False

    return True