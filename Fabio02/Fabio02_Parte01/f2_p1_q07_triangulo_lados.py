def main():
    lado1 = float(input("Digite um lado do triângulo: "))
    lado2 = float(input("Digite um outro lado do triângulo: "))
    lado3 = float(input("Digite um outro lado do triângulo: "))

    triangulo = verificar_triangulo(lado1, lado2, lado3)
    print(triangulo)

def verificar_triangulo(l1, l2, l3):
    if (l1 == 0) or (l2 == 0) or (l3 == 0):
        return "Esses lados não formam um triângulo."
    
    elif (l1 + l2 >= l3) and (l1 + l3 >= l2) and (l2 + l3 >= l1):
        if (l1 == l2 ) and (l2 == l3):
            return "Esses lados formam um triângulo equilátero."
        elif (l1 == l2) or (l1 == l3) or (l2 == l3):
            return "Esses lados formam um triângulo isósceles."
        elif (l1 != l2) and (l1 != l3) and (l2 != l3):
            return "Esses lados formam um triângulo escaleno."
    
    else:
        return "Esses lados não formam um triângulo."


main()