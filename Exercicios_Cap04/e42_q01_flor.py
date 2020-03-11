import turtle
bob = turtle.Turtle()
bob.speed('fastest')

def polygon(t, lenght, n, angle):
    angulo = 360 / n
    for i in range(angle):
        t.fd(lenght)
        t.lt(angulo)

def arc(t, r, angle):
    circumference = 2 * 3.14 * r
    lenght = circumference / 360
    polygon(t, lenght, 360, angle)

def petala(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)

def flor(t, n, r, angle):
    for i in range(n):
        petala(t, r, angle)
        t.lt(360 / n)

def move_caneta(t, length):
    t.pu()
    t.fd(length)
    t.pd()


move_caneta(bob, 0)
flor(bob, 7, 60, 60)

move_caneta(bob, 200)
flor(bob, 10, 60, 80)

move_caneta(bob, - 400)
flor(bob, 20, 60, 40)

turtle.mainloop()
