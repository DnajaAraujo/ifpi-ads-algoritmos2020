def main():
    turno = input("Digite o seu turno (M para manhã, V para vespetino ou N para noturno): ")

    turno_analisado = analisa_turno(turno)
    print(turno_analisado)


def analisa_turno(t):
    if t == "M" or t == "m":
        return "Bom Dia!"
    elif t == "V" or t =="v":
        return "Boa Tarde!"
    elif t == "N" or t =="n":
        return "Boa Noite!"
    else:
        return "Valor inválido!"


main()
