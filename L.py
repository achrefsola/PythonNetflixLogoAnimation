import turtle


def turtle_L1(x,y,s):
    l1x=-x//4+s
    l1y=0
    l_heigh=y//2
    l_width=y//10
    tur=turtle.Turtle()
    tur.hideturtle()
    tur.pencolor("#c51c1f") 
    tur.pensize(1)
    tur.speed(0)
    tur.penup()
    tur.goto(l1x,l1y)
    tur.setheading(90)
    tur.pendown()
    tur.fillcolor("#c51c1f")
    tur.begin_fill()

    for i in range(2):
        
        tur.forward(l_heigh)
        tur.right(90)
        tur.forward(l_width)
        tur.right(90)
    tur.end_fill()


def turtle_L2(x,y,s):
    l1x=-x//4+s
    l1y=0
    tur2=turtle.Turtle()
    tur2.hideturtle()
    tur2.pencolor("#c51c1f") 
    tur2.pensize(1)
    tur2.speed(0)
    tur2.penup()
    tur2.goto(l1x,l1y)
    tur2.pendown()
    tur2.fillcolor("#c51c1f")
    tur2.begin_fill()

    for i in range(2):
        tur2.forward(100)
        tur2.left(90)
        tur2.forward(50)
        tur2.left(90)
    tur2.end_fill()




