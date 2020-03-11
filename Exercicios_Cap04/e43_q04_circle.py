import turtle
bob = turtle.Turtle()

def polygon(t, lenght, n):
    angulo = 360 / n
    for i in range(n):
        t.fd(lenght)
        t.lt(angulo)

def circle(t, r):
    circumference = 2 * 3.14 * r
    lenght = circumference / 360
    polygon(t, lenght, 360)


circle(bob, 100)
turtle.mainloop()