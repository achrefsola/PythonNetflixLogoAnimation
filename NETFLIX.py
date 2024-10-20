import turtle

from N import turtle_N1,turtle_N2,turtle_N3
from E import turtle_E1,turtle_E2
from T import turtle_T1,turtle_T2
from F import turtle_F1,turtle_F2
from L import turtle_L1,turtle_L2
from I import turtle_I1
from X import turtle_X1,turtle_X2




turtle.bgcolor("black")
x=1000
y=500

turtle.setup(width=1.0,height=1.0)




turtle_N1(x,y)
turtle_N2(x,y)
turtle_N3(x,y)
turtle_E1(x,y,-225)
turtle_E2(x,y,-225)
turtle_T1(x,y,0)
turtle_T2(x,y,0)
turtle_F1(x,y,150)
turtle_F2(x,y,150)
turtle_L1(x,y,300)
turtle_L2(x,y,300)
turtle_I1(x,y,450)
turtle_X1(x,y,550)
turtle_X2(x,y,550)

turtle.exitonclick()
