def main():
    a = float(input("Digite a medida do lado 'a' de um triângulo retângulo: "))
    b = float(input("Digite a medida do lado 'b' de um triângulo retângulo: "))
    c = float(input("Digite a medida do lado 'c' de um triângulo retângulo: "))

    hipotenusa = encontra_hipotenusa(a, b, c)
    print(hipotenusa)


def encontra_hipotenusa(a, b, c):
    if (a**2) == ((b**2) + (c**2)):
        return "O  lado 'a' é a hipotenusa, os lados 'b' e 'c' são catetos."
    elif (b**2) == ((a**2) + (c**2)):
        return "O  lado 'b' é a hipotenusa, os lados 'a' e 'c' são catetos."
    elif (c**2) == ((a**2) + (b**2)):
        return "O  lado 'c' é a hipotenusa, os lados 'a' e 'b' são catetos."
    else:
        return "Esses lados não formam um triângulo retângulo."

    
main()
