import turtle
bob = turtle.Turtle()

def polygon(t, lenght, n):
    angulo = 360 / n
    for i in range(n):
        t.fd(lenght)
        t.lt(angulo)


polygon(bob, 100, 7)
turtle.mainloop()