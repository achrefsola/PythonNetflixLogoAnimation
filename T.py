import turtle


def turtle_T1(x,y,s):
    t1x=-x//4+s
    t1y=0
    t_heigh=y//2
    t_width=y//10
    tur2=turtle.Turtle()
    tur2.hideturtle()
    tur2.pencolor("#c51c1f") 
    tur2.pensize(1)
    tur2.speed(0)
    tur2.penup()
    tur2.goto(t1x-50,t1y+t_heigh)
    tur2.pendown()
    tur2.fillcolor("#c51c1f")
    tur2.begin_fill()

    for i in range(2):
        tur2.forward(150)
        tur2.right(90)
        tur2.forward(50)
        tur2.right(90)
    tur2.end_fill()


def turtle_T2(x,y,s):
    t1x=-x//4+s
    t1y=0
    t_heigh=y//2
    t_width=y//10
    tur=turtle.Turtle()
    tur.hideturtle()
    tur.pencolor("#c51c1f") 
    tur.pensize(1)
    tur.speed(0)
    tur.penup()
    tur.goto(t1x,t1y)
    tur.setheading(90)
    tur.pendown()
    tur.fillcolor("#c51c1f")
    tur.begin_fill()

    for i in range(2):
        
        tur.forward(t_heigh)
        tur.right(90)
        tur.forward(t_width)
        tur.right(90)
    tur.end_fill()




