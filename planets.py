import turtle

# Create our t1 turtle
t1 = turtle.Turtle()
t1.shape("turtle")
t1.speed(0)
t1.width(3)
t1.color("yellow", "red")

# Create our t2 turtle
t2 = turtle.Turtle()
t2.shape("turtle")
t2.speed(0)
t2.width(3)
t2.color("blue", "orange")

# Create our t3 turtle
t3 = turtle.Turtle()
t3.shape("turtle")
t3.speed(0)
t3.width(3)
t3.color("red", "blue")

# Move t1 to its starting position
t1.penup()
t1.goto(150, 150)
t1.pendown()

# Move t2 to its starting position
t2.penup()
t2.goto(-150, -150)
t2.pendown()

# Move t3 to its starting position
t3.penup()
t3.goto(-150, 150)
t3.pendown()

# Define our draw_box function
def draw_box(t):
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.end_fill()


# Create our list of turtles
turtles = [t1, t2, t3]

# Create our for loop for 36 petals of the flower
for petal in range(36):

    # Create our for loop to draw a flower petal with
    # each turtle in the turtles list
    for a_turtle in turtles:

        # Draw and rotate each turtle
        draw_box(a_turtle)
        a_turtle.right(10)

