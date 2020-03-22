def main():
    angulo1 = float(input("Digite um ângulo interno: "))
    angulo2 = float(input("Digite um outro ângulo interno: "))
    angulo3 = float(input("Digite um outro ângulo interno: "))

    triangulo = verificar_triangulo(angulo1, angulo2, angulo3)
    print(triangulo)


def verificar_triangulo(a1, a2, a3):
    if (a1 + a2 + a3) == 180:
        if (a1 < 90) and (a2 < 90) and (a3 < 90):
            return "Esses ângulos internos formam um triângulo acutângulo."
        elif (a1 == 90) or (a2 == 90) or (a3 == 90):
            return "Esses ângulos internos formam um triângulo retângulo."
        elif (a1 > 90) and (a2 > 90) and (a3 > 90):
            return "Esses ângulos internos formam um triângulo obtusângulo."
    
    else:
        return "Esses ângulos internos não formam um triângulo."


main()
