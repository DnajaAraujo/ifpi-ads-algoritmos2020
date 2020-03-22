def main():
    letra = input("Digite uma letra: ")

    letra_verificada = verifica_letra(letra)
    print(letra_verificada)


def verifica_letra(l):
    if (l == "a" or l == "e" or l == "i" or l == "o" or l =="u") or (l == "A" or l == "E" or l == "I" or l == "O" or l =="U"):
        return f"A letra '{l}' é uma vogal."
    else:
        return f"A letra '{l}' é uma consoante."


main()