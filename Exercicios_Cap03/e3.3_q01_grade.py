def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def linha_tipo1():
    print("+ - - - -", end = " ")

def linha_tipo2():
    print("|        ", end = " ")

def print_linha_1():
    do_twice(linha_tipo1)
    print("+")
    
def print_linha_2():
   do_twice(linha_tipo2)
   print("|")

def linha_grade():
    print_linha_1()
    do_four(print_linha_2)

def grade():
    do_twice(linha_grade)
    print_linha_1()


grade()

