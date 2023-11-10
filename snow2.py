import turtle
import random

wn = turtle.Screen()
wn.bgcolor("grey")

colors = ["cyan", "purple", "white", "blue"]

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
    snowflakes = []  # List to store snowflake information (turtle, position, size)

    for _ in range(num_snowflakes):
        elsa = turtle.Turtle()
        elsa.speed("fastest")  # Set the drawing speed to the fastest
        elsa.penup()
        elsa.setx(random.randint(-200, 200))
        elsa.sety(random.randint(-200, 200))
        elsa.pendown()
        elsa.color(random.choice(colors))
        size = random.randint(10, 50)  # Random size
        elsa.pensize(size // 10)  # Adjust pen size based on snowflake size
        branch(elsa, size)
        elsa.hideturtle()  # Hide the turtle after drawing a snowflake
        snowflakes.append((elsa, size))  # Store snowflake information

    wn.update()  # Update the screen after drawing all snowflakes

    # Function to make snowflakes fall
    def fall_snowflakes():
        for i, (elsa, size) in enumerate(snowflakes):
            x, y = elsa.position()
            elsa.sety(y - 2)  # Adjust the Y-coordinate to make it fall
            if y - size < -300:  # Check if snowflake reaches the bottom
                elsa.hideturtle()  # Hide the snowflake when it reaches the bottom
                snowflakes[i] = (None, size)  # Mark as done falling

    # Continuously update snowflake positions
    while any(elsa is not None for elsa, _ in snowflakes):
        fall_snowflakes()
        wn.update()

create_snowflakes(5)  # Adjust the number of snowflakes as desired

wn.exitonclick()
