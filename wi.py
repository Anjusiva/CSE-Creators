import turtle
wn=turtle.Screen()
s1=turtle.Turtle()
s1.speed(0)
s1.up()
s1.goto(260,-230)
s1.color("white")
s1.write("Global Warming",move=False,align='center',font=('TIMES NEW ROMAN',18,'underline'))
s1.goto(280,-120)
s1.down()
image="GW2.gif"
wn.addshape(image)
s1.shape(image)
