def do_twice(f, valor):
    f(valor)
    f(valor)

def print_spam(valor):
    print(valor)

def print_twice(valor):
    print(valor)
    print(valor)

def do_four(f, valor):
    do_twice(f, valor)
    do_twice(f, valor)


do_four(print_spam, 'spam')