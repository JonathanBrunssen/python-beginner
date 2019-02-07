
#testDrawing
import turtle
t = turtle.Pen()
t.pencolor("yellow")
turtle.bgcolor("black")
t.pensize(5)
t.speed(0)

#draws the head
t.circle(100)

#draws the right eye
t.penup()
t.setpos(25,150)
t.pendown()
t.right(90)
t.forward(50)

#draws the left eye
t.penup()
t.setpos(-25,150)
t.pendown()
t.forward(50)

#draws the mouth
t.penup()
t.setpos(0,50)
t.pendown()
t.left(90)
t.forward(50)
t.right(180)
t.forward(100)

#draws the corners of the mouth
t.right(45)
t.forward(30)
t.left(180)
t.forward(30)
t.left(45)
t.forward(100)
t.left(45)
t.forward(30)

#moves the cursor out of the way of the face
t.penup()
t.setpos(-100,-100)










