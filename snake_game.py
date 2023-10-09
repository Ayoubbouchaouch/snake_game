#test for the turtle module
import turtle
import time
import random
delay = 0.1
wn = turtle.Screen()
wn.title("Snake game 101")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)
# declaring the segment list
segments = []
# the head of the turtle
head = turtle.Turtle()
head.color("black")
head.shape("square")
head.goto(0, 0)
head.penup()
head.speed(0)
head.direction = "stop"

# movement functions


def up():
    if head.direction != "down":
        head.direction = "up"


def down():
    if head.direction != "up":
        head.direction = "down"


def right():
    if head.direction != "left":
        head.direction = "right"


def left():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)


# keyboard controlling
wn.listen()
wn.onkeypress(up, "Up")
wn.onkey(down, "Down")
wn.onkey(right, "Right")
wn.onkey(left, "Left")
# the apple
apple = turtle.Turtle()
apple.color("red")
apple.shape("circle")
apple.penup()
apple.goto(100, 100)
apple.speed(0)
apple.direction = "stop"

# main game loop

while True:
    wn.update()
    #move()
    # the movement of the apple after the collision with the head
    if head.distance(apple) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        apple.goto(x, y)
        # declaring the snake's body
        segment = turtle.Turtle()
        segment.color("white")
        segment.shape("square")
        segment.goto(0, 0)
        segment.penup()
        segments.append(segment)
    # moving yhe other segments
    for i in range(len(segments)-1, 0,-1):
        x = segments[i -1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    # border detection
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor()  > 290 or head.ycor() < -290:
        head.goto(0,0)
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        head.direction = "stop"


    # moving the segment 0
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    time.sleep(delay)
#
#








wn.mainloop()

