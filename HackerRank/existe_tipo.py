def existe_numero(string):
    '''Esta funcao verifica se existe numeros na string digitada.'''
    numero = "0123456789"

    for caractere in string:
        for i in numero:
            if caractere == i:
                return True


def existe_upper(string):
    '''Esta funcao verifica se existe letras maiusculas na string digitada.'''
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 

    for caractere in string:
        for i in upper_case:
            if caractere == i:
                return True


def existe_lower(string):
    '''Esta funcao verifica se existe letras minusculas na string digitada.'''
    lower_case = "abcdefghijklmnopqrstuvwxyz"

    for caractere in string:
        for i in lower_case:
            if caractere == i:
                return True


def existe_special_character(string):
    '''Esta funcao verifica se existe caracteres especiais na string digitada.'''
    special_characters = "!@#$%^&*()-+"

    for caractere in string:
        for i in special_characters:
            if caractere == i:
                return True


#help(existe_lower)
