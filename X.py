import turtle

def turtle_X1(x,y,s):
    x1x=-x//4+s
    x1y=0
    x_heigh=y//2
    x_width=y//10
    tur3=turtle.Turtle()
    tur3.hideturtle()
    tur3.pencolor("#e30a13")
    tur3.pensize(1)
    tur3.speed(0)
    tur3.penup()
    tur3.goto(x1x+2*x_width,x1y)
    tur3.fillcolor("#e30a13")
    tur3.begin_fill()
    tur3.pendown()
    tur3.goto(x1x,x1y+x_heigh)
    tur3.right(0)
    tur3.forward(x_width)
    tur3.goto(x1x+3*x_width,x1y)

    tur3.end_fill()



def turtle_X2(x,y,s):
    x1x=-x//4+s
    x1y=0
    x_heigh=y//2
    x_width=y//10
    tur4=turtle.Turtle()
    tur4.hideturtle()
    tur4.pencolor("#e30a13")
    tur4.pensize(1)
    tur4.speed(0)
    tur4.penup()
    tur4.goto(x1x,x1y)
    tur4.fillcolor("#e30a13")
    tur4.begin_fill()
    tur4.pendown()
    tur4.goto(x1x+2*x_width,x1y+x_heigh)
    tur4.right(0)
    tur4.forward(x_width)
    tur4.goto(x1x+x_width,x1y)

    tur4.end_fill()

