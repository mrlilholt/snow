import turtle
import random

wn = turtle.Screen()
wn.bgcolor("cyan")

colors = ["grey", "purple", "white", "blue"]

# Function to draw a single branch
def branch(elsa, size):
    for _ in range(8):  # Draw 8 branches for each snowflake
        for i in range(3):
            for i in range(3):
                elsa.forward(size)
                elsa.backward(size)
                elsa.right(45)
            elsa.left(90)
            elsa.backward(size)
            elsa.left(45)
        elsa.right(90)
        elsa.forward(size)
        elsa.right(45)

# Function to create and position multiple snowflakes
def create_snowflakes(num_snowflakes):
    wn.tracer(0)  # Disable screen updates
    for _ in range(num_snowflakes):
        elsa = turtle.Turtle()
        elsa.speed("fastest")  # Set the drawing speed to the fastest
        elsa.penup()
        elsa.setx(random.randint(-200, 200))
        elsa.sety(random.randint(-200, 200))
        elsa.pendown()
        elsa.color(random.choice(colors))
        size = random.randint(3, 50)  # Random size
        elsa.pensize(size // 10)  # Adjust pen size based on snowflake size
        branch(elsa, size)
        elsa.hideturtle()  # Hide the turtle after drawing a snowflake
    wn.update()  # Update the screen after drawing all snowflakes

create_snowflakes(20)  # Adjust the number of snowflakes as desired

wn.exitonclick()
