def main():
    x1 = int(input("Digite a abscissa (x) do 1º ponto:"))
    y1 = int(input("Digite a ordenada (y) do 1º ponto:"))
    x2 = int(input("Digite a abscissa (x) do 2º ponto:"))
    y2 = int(input("Digite a ordenada (y) do 2º ponto:"))

    area_retangulo = calcula_retangulo(x1, y1, x2, y2)
    print(area_retangulo)



def calcula_retangulo(x1, y1, x2, y2):
    if y1 != y2:
        return "Esses pontos não formam um retângulo."
    else:
        distancia1 = (((y1 - 0)**2) + ((x1 - x1)**2)) ** 0.5
        distancia2 = (((y2 - y1)**2) + ((x2 - x1)**2)) ** 0.5

        area = distancia1 * distancia2
        
        if distancia1 == distancia2:
            return f"Esses pontos formam um quadrado de área {area:.1f}"
        else:
            return f"Esses dos pontos formam um retângulo de área {area:.1f}"



main()