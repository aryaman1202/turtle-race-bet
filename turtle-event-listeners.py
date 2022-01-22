import turtle
t = turtle.Turtle()
s = turtle.Screen()


def press_W():
    t.forward(50)


def press_S():
    t.backward(50)


def press_A():
    set_heading = t.heading() + 10
    t.setheading(set_heading)


def press_D():
    set_heading = t.heading() - 10
    t.setheading(set_heading)


def press_C():
    t.clear()
    t.setheading(0)
    t.penup()
    t.goto(0, 0)
    t.pendown()


s.listen()
s.onkey(key="w", fun=press_W)
s.onkey(key="s", fun=press_S)
s.onkey(key="a", fun=press_A)
s.onkey(key="d", fun=press_D)
s.onkey(key="c", fun=press_C)
s.exitonclick()
