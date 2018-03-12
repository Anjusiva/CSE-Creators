#war
p4=turtle.Turtle()
p4.speed(10)
p4.color("red")
p4.up()
p4.goto(50,50)
p4.write("WAR",move=False,align='left',font=('Arial',15,'underline'))
p4.right(90)
p4.forward(70)
p4.left(90)
image="war1.gif"
image2="war2.gif"
wn.addshape(image)
p4.forward(60)
p4.shape(image)
p5=turtle.Turtle()
p5.goto(150,-130)
wn.addshape(image2)
p5.shape(image2)



p9=turtle.Turtle()
p9.up()
p9.color("red")
p9.goto(250,200)
p9.write("Atrocities to Women",move=False,align='center',font=('Arial',15,'underline'))
p9.goto(250,130)
image3="women.gif"
wn.addshape(image3)
p9.shape(image3)
p10=turtle.Turtle()
p10.up()
p10.goto(280,-150)
image4="GW.gif"
wn.addshape(image4)
p10.shape(image4)




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
            a_turtle.right(10)


colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    for x in range(22):
        t.pencolor(colors[x%6])
        t.width(3)
        t.forward(x)
        t.left(59)
for s in turtles:
    draw(s)
    
   
