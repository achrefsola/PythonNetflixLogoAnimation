import turtle


def turtle_N1(x,y):
    
    n1x=-turtle.window_width()//2
    n1y=0
    n_heigh=y//2
    n_width=y//10
    tur=turtle.Turtle()
    tur.hideturtle()
    tur.pencolor("#c51c1f") 
    tur.pensize(1)
    tur.speed(0)
    tur.penup()
    tur.goto(n1x,n1y)
    tur.setheading(90)
    tur.pendown()
    tur.fillcolor("#c51c1f")
    tur.begin_fill()

    for i in range(2):
        
        tur.forward(n_heigh)
        tur.right(90)
        tur.forward(n_width)
        tur.right(90)
    tur.end_fill()


def turtle_N2(x,y):
    n1x=-turtle.window_width()//2
    n1y=0
    n_heigh=y//2
    n_width=y//10
    n_endx=n1x+2*n_width
    n_endy=n1y
    
    

    tur2=turtle.Turtle()
    tur2.hideturtle()
    tur2.pencolor("#c51c1f")
    tur2.pensize(1)
    tur2.speed(0)
    tur2.penup()
    tur2.goto(n1x+2*n_width,n1y)
    tur2.setheading(90)
    tur2.pendown()

    tur2.fillcolor("#c51c1f")
    tur2.begin_fill()

    for i in range(2):
        tur2.forward(n_heigh)
        tur2.right(90)
        tur2.forward(n_width)
        tur2.right(90)

    tur2.end_fill()


def turtle_N3(x,y):
    n1x=-turtle.window_width()//2
    n1y=0
    n_heigh=y//2
    n_width=y//10

    tur3=turtle.Turtle()
    tur3.hideturtle()
    tur3.pencolor("#e30a13")
    tur3.pensize(1)
    tur3.speed(10)
    tur3.penup()
    tur3.goto(n1x+2*n_width,n1y)
    tur3.fillcolor("#e30a13")
    tur3.begin_fill()
    tur3.pendown()
    tur3.goto(n1x,n1y+n_heigh)
    tur3.right(0)
    tur3.forward(n_width)
    tur3.goto(n1x+3*n_width,n1y)

    tur3.end_fill()



