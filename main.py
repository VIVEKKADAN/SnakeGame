import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(width=700, height=700)
screen.bgcolor("#1d1d1d")
screen.tracer(0)

# Create border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("red")
border_pen.penup()
border_pen.goto(-310, 250)
border_pen.pendown()
border_pen.pensize(4)
for _ in range(2):
    border_pen.forward(600)
    border_pen.right(90)
    border_pen.forward(500)
    border_pen.right(90)
border_pen.hideturtle()

# Snake head
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# Food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("circle")
fruit.color("white")
fruit.penup()
fruit.goto(30, 30)

# Scoring
score = 0
delay = 0.1

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 300)
score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))

# Function to move the snake
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

# Functions to change the snake's direction
def go_up():
    if snake.direction != "down":
        snake.direction = "up"

def go_down():
    if snake.direction != "up":
        snake.direction = "down"

def go_right():
    if snake.direction != "left":
        snake.direction = "right"

def go_left():
    if snake.direction != "right":
        snake.direction = "left"

# Keyboard bindings
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_right, "d")
screen.onkeypress(go_left, "a")

# Main game loop
old_fruit = []
while True:
    screen.update()

    # Check for a collision with the border
    if (
        snake.xcor() > 290
        or snake.xcor() < -290
        or snake.ycor() > 240
        or snake.ycor() < -240
    ):
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "stop"
        score = 0
        score_pen.clear()
        score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))

    # Check for a collision with the food
    if snake.distance(fruit) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-230, 230)
        fruit.goto(x, y)

        # Add a segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        old_fruit.append(new_segment)

        # Increase the score
        score += 10
        score_pen.clear()
        score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))

        # Increase the speed of the snake
        delay -= 0.001

    # Move the end segments first in reverse order
    for index in range(len(old_fruit) - 1, -1, -1):
        x = old_fruit[index - 1].xcor() if index > 0 else snake.xcor()
        y = old_fruit[index - 1].ycor() if index > 0 else snake.ycor()
        old_fruit[index].goto(x, y)

    move()

    # Check for body collisions
    for segment in old_fruit:
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = "stop"

            # Hide the segments
            for seg in old_fruit:
                seg.goto(1000, 1000)

            old_fruit.clear()

            # Reset the score
            score = 0
            score_pen.clear()
            score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))

    time.sleep(delay)

turtle.done()
