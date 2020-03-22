def main():
    numero = int(input("Digite um número inteiro menor que 1000: "))

    numero_c_d_u = calcula_numero_c_d_u(numero)
    print(numero_c_d_u)


def calcula_numero_c_d_u(n):
    centena = n // 100
    resto = n % 100

    dezena = resto // 10
    unidade = resto % 10

    nova_centena = ""
    nova_dezena = ""
    nova_unidade = ""
    
    if (len(str(n)) > 3) or (n == 0):
        return "Erro: Número inválido para esta operação!"
    else:
        #centena
        if centena >= 2:
            if dezena != 0:
                if unidade != 0:
                    nova_centena = str(centena) + " centenas, "
                else:
                    nova_centena = str(centena) + " centenas e "
            else:
                if unidade != 0:
                    nova_centena = str(centena) + " centenas e "
                else:
                    nova_centena = str(centena) + " centenas "

        elif centena < 2 and centena != 0:
            if dezena != 0:
                if unidade != 0:
                    nova_centena = str(centena) + " centena, "
                else:
                    nova_centena = str(centena) + " centena e "
            else:
                if unidade != 0:
                    nova_centena = str(centena) + " centena e "
                else:
                    nova_centena = str(centena) + " centena "
                
        #dezena
        if dezena >= 2:
            if unidade != 0:
                nova_dezena = str(dezena) + " dezenas e "
            else:
                nova_dezena = str(dezena) + " dezenas "

        elif dezena < 2 and dezena != 0:
            if unidade != 0:
                nova_dezena = str(dezena) + " dezena e "
            else:
                nova_dezena = str(dezena) + " dezena "

        #unidade
        if unidade >= 2:
            nova_unidade = str(unidade) + " unidades"
        elif unidade < 2 and unidade != 0:
            nova_unidade = str(unidade) + " unidade"


        return f"{n} = {nova_centena}{nova_dezena}{nova_unidade}"


main() 