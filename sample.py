import turtle
wn=turtle.Screen()
c=turtle.Turtle()

c.circle(12)

c.right(90)
c.forward(30)
c.right(15)
c.forward(20)
c.backward(20)
c.left(30)
c.forward(20)
c.backward(20)
c.left(170)
c.up()
c.forward(20)
c.left(120)
c.down()
c.forward(25)
c.backward(25)
c.left(120)
c.forward(30)



def man1(c):
    c.begin_fill()
    c.circle(12)
    c.end_fill()
    c.right(50)
    c.forward(30)
    c.right(15)
    c.forward(20)
    c.backward(20)
    c.left(30)
    c.forward(20)
    c.backward(20)
    c.left(170)
    c.up()
    c.forward(20)
    c.left(120)
    c.down()
    c.forward(25)
    c.backward(25)
    c.left(120)
    c.forward(30)
man1(p7)
p7.up()
p7.goto(200,180)
p7.down()
man1(p7)
p7.up()
p7.goto(250,90)
p7.down()
man1(p7)




p11.color("blue")
p11.up()
p11.goto(-250,0)
p11.forward(25)
p11.left(90)
p11.down()
p11.width(50)
p11.forward(300)
