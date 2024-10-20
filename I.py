import turtle



def turtle_I1(x,y,s):
    i1x=-x//4+s
    i1y=0
    i_heigh=y//2
    i_width=y//10
    tur=turtle.Turtle()
    tur.hideturtle()
    tur.pencolor("#c51c1f") 
    tur.pensize(1)
    tur.speed(0)
    tur.penup()
    tur.goto(i1x,i1y)
    tur.setheading(90)
    tur.pendown()
    tur.fillcolor("#c51c1f")
    tur.begin_fill()

    for i in range(2):
        
        tur.forward(i_heigh)
        tur.right(90)
        tur.forward(i_width)
        tur.right(90)
    tur.end_fill()



