def do_twice(f, valor):
    f(valor)
    f(valor)

def print_spam(valor):
    print(valor)

def print_twice(valor):
    print(valor)
    print(valor)


do_twice(print_twice, 'spam')