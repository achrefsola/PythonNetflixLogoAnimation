import turtle




def turtle_F1(x,y,s):
    f1x=-x//4+s
    f1y=0
    f_heigh=y//2
    f_width=y//10
    tur=turtle.Turtle()
    tur.hideturtle()
    tur.pencolor("#c51c1f") 
    tur.pensize(1)
    tur.speed(0)
    tur.penup()
    tur.goto(f1x,f1y)
    tur.setheading(90)
    tur.pendown()
    tur.fillcolor("#c51c1f")
    tur.begin_fill()

    for i in range(2):
        
        tur.forward(f_heigh)
        tur.right(90)
        tur.forward(f_width)
        tur.right(90)
    tur.end_fill()


def turtle_F2(x,y,s):
    f1x=-x//4+s
    f1y=0
    f_heigh=y//2
    f_width=y//10
    tur2=turtle.Turtle()
    tur2.hideturtle()
    tur2.pencolor("#c51c1f") 
    tur2.pensize(1)
    tur2.speed(0)
    tur2.penup()
    tur2.goto(f1x,f1y+f_heigh)
    tur2.pendown()
    tur2.fillcolor("#c51c1f")
    tur2.begin_fill()

    for i in range(2):
        tur2.forward(100)
        tur2.right(90)
        tur2.forward(50)
        tur2.right(90)
    tur2.end_fill()

    tur2.penup()
    tur2.goto(f1x,f1y+(f_heigh//2)+25)
    tur2.pendown()
    tur2.fillcolor("#c51c1f")
    tur2.begin_fill()

    for i in range(2):
        tur2.forward(100)
        tur2.right(90)
        tur2.forward(50)
        tur2.right(90)
    tur2.end_fill()



