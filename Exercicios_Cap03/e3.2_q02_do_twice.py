def do_twice(f, valor):
    f(valor)
    f(valor)

def print_spam(valor):
    print(valor)


do_twice(print_spam, 'monty')