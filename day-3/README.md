# python-beginner-plans

## Day 3:

---

### Smiley Face Drawing

This program introduces the kids to the python turtle. It's a simple series of commands that ends up drawing a smiley face, seen below.

![smiley-face-drawing](https://github.com/Fun2LearnCode/python-beginner-plans/blob/master/resources/smiley-face-drawing.png)

```python
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
```

---

### Create your own drawing

At this point, put some basic turtle commands on the screen and let the kids attempt to make their own drawings. *Let them know that the turtle always starts in the center of the screen (at (0,0)) and facing to the right.*

First set:
```python
t = turtle.Pen()
```
so that everyone will have the same pen tool.

#### Here is the list of turtle commands:

Command | Description
----|----
t.forward(pixels) | Moves the pen forward the specified amount of pixels
t.right(angle) | Turns the pen to the right the specified amount of radians
t.left(angle) | Turns the pen to the left the specified amount of radians
t.circle(radius) | Draws a circle with the specified radius
t.penup() | Picks the pen up, use this before changing the pen's position
t.setpos(x,y) | Moves the pen to the specified location in pixels
t.pendown() | Puts the pen back down to continue drawing after you move the pen
t.pencolor('color') | Changes the pen's color

**TODO: Update this table with any other important turtle commands**

---

### Color Spiral

```python
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.pencolor("green")
t.speed(0)
for x in range(1000):
    t.forward(x)
    t.left(95)
```

This is a very simple program used to explain looping in python. Once the students have this down, allow them to experiment with changing the values to see the different colors/sizes of spirals they can create.

---

## Start on [Spyrographs](https://github.com/Fun2LearnCode/python-beginner-plans/tree/master/day-4) if time allows.
