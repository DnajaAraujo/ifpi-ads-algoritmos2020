def right_justify(s):
    num_espaco = (70 - (len(s))) * " "
    resultado = num_espaco + s
    print(resultado)

right_justify('monty')
