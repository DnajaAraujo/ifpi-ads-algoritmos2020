def main():
    angulo = float(input("Digite a medida do ângulo (de 0 a 360 graus): "))

    quadrante = retorna_quadrante(angulo)
    print(quadrante)


def retorna_quadrante(a):
    if a >= 0 and a <= 90:
        return "Esse ângulo está no primeiro quadrante."
    elif a > 90 and a <= 180:
        return "Esse ângulo está no segundo quadrante."
    elif a > 180 and a <= 270:
        return "Esse ângulo está no terceiro quadrante."
    elif a > 270 and a <= 360:
        return "Esse ângulo está no quarto quadrante."
    else:
        return "Essa medida de ângulo não existe."


main()