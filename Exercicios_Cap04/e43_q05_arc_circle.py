import turtle
bob = turtle.Turtle()

def polygon(t, lenght, n, angle):
    angulo = 360 / n
    for i in range(angle):
        t.fd(lenght)
        t.lt(angulo)

def arc(t, r, angle):
    circumference = 2 * 3.14 * r
    lenght = circumference / 360
    polygon(t, lenght, 360, angle)


arc(bob, 100, 90)
turtle.mainloop()