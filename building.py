import turtle
wn1=turtle.Screen()
b=turtle.Turtle()
b.up()
b.goto(-250,180)
b.write("Farming and Industrialization",move=False,align='center',font=('TIMES NEW ROMAN',18,'underline'))
b.goto(-280,50)
b.left(90)
b.down()
b.speed(0)
def build(b0):
    b0.width(5)
    b0.color("black","AntiqueWhite4")
    b0.begin_fill()
    b0.forward(30)
    b0.right(90)
    b0.forward(10)
    b0.right(90)
    b0.forward(30)
    b0.end_fill()
build(b)
b.left(90)
b.forward(20)
b.left(90)
def build1(b1):
    b1.width(5)
    b1.color("black","violet")
    b1.begin_fill()
    b1.forward(20)
    b1.right(70)
    b1.forward(10)
    b1.left(70)
    b1.forward(10)
    b1.right(90)
    b1.forward(10)
    b1.right(90)
    b1.forward(40)
    b1.left(90)
    b1.end_fill()
build1(b)
b.up()
b.goto(-360,120)
b.up()
b.forward(10)
b.left(90)
b.down()
build(b)
b.left(90)
b.forward(10)
b.left(90)
build1(b)
b.forward(10)
b.left(90)
b.down()
build(b)
b.left(90)
b.forward(10)
b.left(90)
build1(b)
b.up()
b.forward(20)
b.down()
b.left(90)
build(b)
b.left(90)
b.forward(10)
b.left(90)
build1(b)
b.up()
b.goto(-200,150)
b.down()
b.left(90)
build(b)
b.left(90)
b.forward(10)
b.left(90)
build1(b)
b.hideturtle()
