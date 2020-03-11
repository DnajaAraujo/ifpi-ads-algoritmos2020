import turtle
bob = turtle.Turtle()

def square(t):
    for i in range(4):
        bob.fd(t)
        bob.lt(90)


square(100)
turtle.mainloop()
    