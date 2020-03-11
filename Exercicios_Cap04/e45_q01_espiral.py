import turtle
bob = turtle.Turtle()

def espiral(t, tam_inicial, num_voltas):
    for i in range(num_voltas):
        t.fd(tam_inicial + i)
        t.lt(10)


espiral(bob, 0, 100)

turtle.mainloop()