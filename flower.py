import turtle
wn=turtle.Screen()
#flower1
f1=turtle.Turtle()
f1.up()
f1.goto(-400,-150)
f1.down()
f1.speed(0)
#flower2
f2=turtle.Turtle()
f2.up()
f2.goto(-300,-150)
f2.down()
f2.speed(0)
#flower3
f3=turtle.Turtle()
f3.up()
f3.goto(-100,-100)
f3.down()
f3.speed(0)
#flower 4
f4=turtle.Turtle()
f4.up()
f4.goto(-165,-180)
f4.down()
f4.speed(0)
#flower5
f5=turtle.Turtle()
f5.up()
f5.goto(-150,-60)
f5.down()
f5.speed(0)
#flower6
f6=turtle.Turtle()
f6.up()
f6.goto(-350,-60)
f6.down()
f6.speed(0)
turtles = [f1, f2, f3, f4,f5,f6]
for t1 in turtles:
    t1.left(90)
    t1.color("SpringGreen4")
    t1.width(5)
    t1.forward(50)
    t1.right(90)
def draw(t):
    t.color("red","pink")
    t.speed(0)
    t.begin_fill()
    t.forward(8)
    t.right(90)
    t.forward(8)
    t.right(90)
    t.forward(8)
    t.right(90)
    t.forward(8)
    t.right(90)
    t.end_fill()
    t.hideturtle()
for petal in range(10):
    for a_turtle in turtles:
            draw(a_turtle)
            a_turtle.speed(0)
            a_turtle.right(10)
