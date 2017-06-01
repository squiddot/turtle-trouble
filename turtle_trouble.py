import turtle
import random

def getHeading():
    heading1 = random.randint(15,75)
    return(heading1)

def keyUp():
    user.forward(25)
    return

def keyLeft():
    user.speed(0)
    user.left(90)
    user.forward(25)
    user.right(90)
    user.speed(1)
    return

def keyRight():
    user.speed(0)
    user.right(90)
    user.forward(25)
    user.left(90)
    user.speed(1)
    return

def keyDown():
    user.back(25)
    return

def bubble1Move(i):
    bubble1.forward(10)
    if i % 3 == 0:
        if bubble1.ycor()>= 375 or bubble1.ycor() <= -375:
            bubble1.speed(0)
            bubble1.seth(bubble1BounceY())
            bubble1.speed(1)
        if bubble1.xcor()>= 375 or bubble1.xcor() <= -375:
            bubble1.speed(0)
            bubble1.seth(bubble1BounceX())
            bubble1.speed(1)
    return

def bubble1BounceY():
    newheading = 360 - (bubble1.heading())
    if newheading < 0:
        newheading += 360
    return(int(newheading))

def bubble1BounceX():
    newheading = 180 - (bubble1.heading())
    if newheading < 0:
        newheading += 360
    return(int(newheading))

def bubble2Move(i):
    bubble2.forward(15)
    if i % 3 == 0:
        if bubble2.ycor()>= 375 or bubble2.ycor() <= -375:
            bubble2.speed(0)
            bubble2.seth(bubble2BounceY())
            bubble2.speed(1)
        if bubble2.xcor()>= 375 or bubble2.xcor() <= -375:
            bubble2.speed(0)
            bubble2.seth(bubble2BounceX())
            bubble2.speed(1)
    return

def bubble2BounceY():
    newheading = 360 - (bubble2.heading())
    if newheading < 0:
        newheading += 360
    return(int(newheading))

def bubble2BounceX():
    newheading = 180 - (bubble2.heading())
    if newheading < 0:
        newheading += 360
    return(int(newheading))

def nextLevel(points):
    difficulty = (points // 300)*2
    bubble1.turtlesize(difficulty)
    bubble2.turtlesize(difficulty)
    bubble1.speed(difficulty)
    bubble2.speed(difficulty)
    level = (points // 300)
    display1.clear()
    if level == 1:
        display1.write("LEVEL TWO")
    if level == 2:
        display1.write("LEVEL THREE")
    if level == 3:
        display1.write("LEVEL FOUR")
    if level == 4:
        display1.write("LEVEL FIVE")
    if level == 5:
        display1.write("LEVEL SIX")
    return (difficulty)

def bump(lives,difficulty):
    if user.xcor() > (bubble1.xcor()- ((difficulty*10)+30)) and user.xcor()< (bubble1.xcor()+ ((difficulty*10)+30)):
        if user.ycor() > (bubble1.ycor() -((difficulty*10)+30)) and user.ycor() < (bubble1.ycor()+((difficulty*10)+30)):
            bubble1.write("POP!")
            lives = lives - 1
            display2.clear()
            if lives == 2:
                display2.write("TWO LIVES LEFT")
            if lives == 1:
                display2.write("ONE LIFE LEFT")
            if lives <= 0:
                display2.write("GAME OVER!")
    if user.xcor() > (bubble2.xcor()- ((difficulty*10)+30)) and user.xcor()< (bubble2.xcor()+((difficulty*10)+30)):
        if user.ycor() > (bubble2.ycor() - ((difficulty*10)+30)) and user.ycor() < (bubble2.ycor()+ ((difficulty*10)+30)):
            bubble2.write("POP!")
            lives = lives - 1
            display2.clear()
            if lives == 2:
                display2.write("TWO LIVES LEFT")
            if lives == 1:
                display2.write("ONE LIFE LEFT")
            if lives <= 0:
                display2.write("GAME OVER!")
    return (lives)

def gameOver():
    bubble1.reset()
    bubble1.hideturtle()
    bubble2.reset()
    bubble2.hideturtle()
    user.hideturtle()
    display2.clear()
    display3.clear()
    display1.clear()


scrn = turtle.Screen()
scrn.setup(width=750, height=750)
scrn.bgcolor("midnightblue")
scrn.title("Turtle Trouble")

bubble1 = turtle.Turtle()
bubble1.color("white")
bubble1.shape("circle")
bubble1.turtlesize(1)
bubble1.penup()
bubble1.speed(2)

bubble2 = turtle.Turtle()
bubble2.color("white")
bubble2.shape("circle")
bubble2.turtlesize(1)
bubble2.penup()
bubble2.speed(2)

display1 = turtle.Turtle()
display1.hideturtle()
display1.penup()
display1.color("aqua")
display1.left(90)
display1.forward(350)
display1.write("LEVEL ONE")

display2 = turtle.Turtle()
display2.hideturtle()
display2.penup()
display2.color("aqua")
display2.left(90)
display2.forward(325)
display2.write("3 LIVES LEFT")

display3 = turtle.Turtle()
display3.hideturtle()
display3.penup()
display3.color("aqua")
display3.left(90)
display3.forward(300)

user = turtle.Turtle()
user.shape("turtle")
user.turtlesize(4)
user.penup()
user.color("mediumspringgreen")
user.seth(90)

heading1 = getHeading()
bubble1.setheading(heading1)

heading2 = getHeading()
bubble2.setheading(heading2)

scrn.onkey(keyUp, "Up")
scrn.onkey(keyLeft, "Left")
scrn.onkey(keyRight, "Right")
scrn.onkey(keyDown, "Down")

game="continue"
i = 0
lives = 3
difficulty = 1

scrn.listen()
while game == "continue":
    bubble1Move(i)
    bubble2Move(i)
    i += 1
    display3.clear()
    display3.write(i)
    if i % 300 == 0:
        difficulty = nextLevel(i)
    if i > 10 and i % 3 == 0:
       lives = bump(lives,difficulty)
    if lives <= 0:
        gameOver()
        game = "stop"

display2.home()
display2.write("Congrats! Your score is " + str(i) +" points!\n Thanks for playing Turtle Trouble!\n Click anywhere to close.")
scrn.exitonclick()
scrn.mainloop()
