import turtle


def distance(t1, t2):
    x = t1.xcor() - t2.xcor()
    y = t1.ycor() - t2.ycor()
    return (x**2 + y**2)**0.5


t = turtle.Turtle()
t2 = turtle.Turtle()
t.forward(100)
t.speed(0)

angle = 90
length = 100

for i in range(100):
    length*= 1.01
    angle *= 1.01
    t.pencolor(0.99*(i/100), 0.0, 0.0)
    t.left(angle)
    t.forward(length)
    d =  distance(t, t2)
    if d > 200:


    t2.forward(100)
    t2.left(angle)

